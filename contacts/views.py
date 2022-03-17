from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User


def inquiry(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        car_id = request.POST['car_id']
        customer_need = request.POST['customer_need']
        car_title = request.POST['car_title']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.filter(user_id=user_id, car_id=car_id)
            if has_contacted:
                messages.error(request, 'You have already made inquery for this car')
                return redirect('/cars/'+car_id)

        data = Contact(first_name=first_name, last_name=last_name, car_id=car_id, customer_need=customer_need, car_title=car_title, city=city, state=state, email=email, phone=phone, message=message, user_id=user_id)

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail(
            'New Car Inquiry',
            'You have a new inquiry for the car' + car_title + '. Please login to you admin panel for more info.',
            'pythonemailtesting76@gmail.com',
            [admin_email],
            fail_silently=False,
        )

        data.save()

        messages.success(request, 'You inquiry form submited')

        return redirect('/cars/'+car_id)