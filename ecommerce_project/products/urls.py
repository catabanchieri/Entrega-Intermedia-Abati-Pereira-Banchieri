from django.urls import path
from products.views import products_list, create_product, menu

urlpatterns = [
    path('products_list/', products_list, name='products_list'),
    path('new_product/', create_product, name='create_product'), #ojooooooooo
    path('menu/', menu, name='menu')
]