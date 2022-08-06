from django.urls import path
from products.views import products_list, create_product

urlpatterns = [
    path('products_list/', products_list, name='products_list'),
    path('create_product/', create_product, name='create_product'),
]