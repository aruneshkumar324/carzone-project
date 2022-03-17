from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User


def home(request):
    teams = Team.objects.all()
    feature_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')

    model_fields = Car.objects.values_list('model', flat=True).distinct()
    location_field = Car.objects.values_list('city', flat=True).distinct()
    year_field = Car.objects.values_list('year', flat=True).distinct()
    body_style_field = Car.objects.values_list('body_style', flat=True).distinct()


    data = {
        "teams": teams,
        "feature_cars": feature_cars,
        "all_cars":all_cars, 
        "model_fields": model_fields,
        "location_field": location_field,
        "year_field": year_field,
        "body_style_field": body_style_field,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all()
    return render(request, 'pages/about.html', {"teams":teams})


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        contact_message = f"Name : {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message} "

        send_mail(
            subject,
            contact_message,
            'pythonemailtesting76@gmail.com',
            [admin_email],
            fail_silently=False,
        )

        messages.success(request, 'Thank you for contacting us.')
        return redirect('contact')
    else:
        return render(request, 'pages/contact.html')