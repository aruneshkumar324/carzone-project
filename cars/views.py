from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 1)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    return render(request, 'cars/cars.html', {"cars": paged_cars})


def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
    return render(request, 'cars/car_detail.html', {"single_car": single_car})


def search(request):
    cars = Car.objects.order_by('-created_date')

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    data = {
        "cars": cars
    }
    return render(request, 'cars/search.html', data)