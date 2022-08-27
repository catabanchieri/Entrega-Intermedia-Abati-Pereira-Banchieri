from django.urls import path
from products.views import products_list, create_product, menu, search_products, update_product, delete_product

urlpatterns = [
    path('products_list/', products_list, name='products_list'),
    path('new_product/', create_product, name='create_product'),
    path('menu/', menu, name='menu'),
    path('search_product/', search_products, name='search_products'),
    path('delete_product/<int:pk>/', delete_product, name='delete_product'),
    path('update_product/<int:pk>/', update_product, name='update_product'),
]