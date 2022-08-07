from django.urls import path
from products.views import products_list, create_product, menu, search_products

urlpatterns = [
    path('products_list/', products_list, name='products_list'),
    path('new_product/', create_product, name='create_product'), #ojooooooooo
    path('menu/', menu, name='menu'),
    path('search_products/', search_products, name='search_products')
]