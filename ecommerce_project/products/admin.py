from django.contrib import admin
from products.models import Products, Category

@admin.register(Products)
class Products_admin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'size', 'available', 'created', 'updated']
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
