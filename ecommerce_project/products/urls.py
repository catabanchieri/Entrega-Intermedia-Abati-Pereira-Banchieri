from django.urls import path
from products.views import List_products, Create_product, Update_product, Delete_product, \
    Search_product, Detail_product

urlpatterns = [
    path('new_product/', Create_product.as_view(), name='Create_product'),
    path('products_list/', List_products.as_view(), name='List_products'),    
    path('search_product/', Search_product.as_view(), name='Search_product'),
    path('delete_product/', Delete_product.as_view(), name='Delete_product'),
    path('update_product/', Update_product.as_view(), name='update_product'),
     path('detail_products/', Detail_product.as_view(), name='detail_products'),
]