from django.contrib import admin
from .models import Customer,Product
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'is_active', 'phone','address')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'is_active', 'registrationDate')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
