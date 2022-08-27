from django.urls import path
from products.views import menu, List_products, Create_product, Update_product, Delete_product, Search_product

urlpatterns = [
    path('menu/', menu, name='menu'),
    path('products_list/<int:pk>', List_products.as_view, name='List_products'),
    path('new_product/', Create_product.as_view, name='Create_product'),
    #path('search_product/<int:pk>', Search_product.as_view, name='Search_product'),
    path('delete_product/<int:pk>/', Delete_product.as_view, name='Delete_product'),
    path('update_product/<int:pk>/', Update_product.as_view, name='update_product'),
]