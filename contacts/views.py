from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages


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

        data = Contact(first_name=first_name, last_name=last_name, car_id=car_id, customer_need=customer_need, car_title=car_title, city=city, state=state, email=email, phone=phone, message=message, user_id=user_id)

        data.save()

        messages.success(request, 'You inquiry form submited')

        return redirect('/cars/'+car_id)