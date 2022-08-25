from django.contrib import admin
from products.models import Products

# Register your models here.
@admin.register(Products)
class Products_Admin(admin.ModelAdmin):
    list_display: tuple
    ['name', 'price', 'description', 'stock', 'size', 'is_active']