from django.contrib import admin
from .models import Car
from django.utils.html import format_html


class CarAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html("<img src='{}' width='50' style='border-radius:50' />".format(object.car_photo.url))
    
    thumbnail.short_description = 'Car Photo'

    list_display = ('id', 'thumbnail', 'car_title', 'color', 'model', 'year', 'city', 'body_style', 'fuel_type', 'is_featured')

    list_display_links = ('id', 'thumbnail', 'car_title')

    list_editable = ('is_featured',)

    search_fields = ('id', 'city', 'car_title', 'year', 'color', 'model')

    list_filter = ('city', 'model', 'body_style', 'fuel_type')


# Register your models here.
admin.site.register(Car, CarAdmin)