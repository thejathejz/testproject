from django.contrib import admin
from .models import Customer,Product
# Register your models here.
admin.site.register(Customer)
    lst_display = ('name', 'price', 'description', 'isActive', 'registrationDate')
    list_filter = ('isActive',)
    search_fields = ('name', 'description')

admin.site.register(Product)iiiiiiiiiiiiiiiiiiii
    list_display = ('name', 'price', 'description', 'isActive', 'registrationDate')
    list_filter = ('isActive',)
    search_fields = ('name', 'description')iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii