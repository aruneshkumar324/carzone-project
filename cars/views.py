from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 3)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    model_fields = Car.objects.values_list('model', flat=True).distinct()
    location_field = Car.objects.values_list('city', flat=True).distinct()
    year_field = Car.objects.values_list('year', flat=True).distinct()
    body_style_field = Car.objects.values_list('body_style', flat=True).distinct()


    data = {
        "cars": paged_cars,
        "model_fields": model_fields,
        "location_field": location_field,
        "year_field": year_field,
        "body_style_field": body_style_field,
    }

    return render(request, 'cars/cars.html', data)


def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
    return render(request, 'cars/car_detail.html', {"single_car": single_car})


def search(request):
    cars = Car.objects.order_by('-created_date')

    model_fields = Car.objects.values_list('model', flat=True).distinct()
    location_field = Car.objects.values_list('city', flat=True).distinct()
    year_field = Car.objects.values_list('year', flat=True).distinct()
    body_style_field = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_fields = Car.objects.values_list('transmission', flat=True).distinct()

    # SEARCH BY ANY KEY FROM DESCRIPTION
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)
    
    # SORT BY MODEL
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)
    
    # SORT BY CITY
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)
    
    # SORT BY YEAR
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)
    
    # SORT BY BODY STYLE
    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style=body_style)
    
    # SORT BY PRICE
    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if min_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)


    data = {
        "cars": cars,
        "model_fields": model_fields,
        "location_field": location_field,
        "year_field": year_field,
        "body_style_field": body_style_field,
        "transmission_fields": transmission_fields,
    }
    return render(request, 'cars/search.html', data)