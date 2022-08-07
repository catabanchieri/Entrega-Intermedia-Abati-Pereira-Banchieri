from django.urls import path
from business.views import stores_list, create_store

urlpatterns = [
    path('stores_list/', stores_list, name='stores_list'),
    path('new_store/', create_store, name='new_store'), #ojooooooooo
]