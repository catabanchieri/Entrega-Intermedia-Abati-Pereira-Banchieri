from django.urls import path
from business.views import stores_list, create_store, opinions_list, create_opinion, menu

urlpatterns = [
    path('menu/', menu, name='menu'),
    path('stores_list/', stores_list, name='stores_list'),
    path('new_store/', create_store, name='new_store'), #ojooooooooo
    path('new_opinion/', create_opinion, name='new_opinion'), #ojooooooooo
    path('opinions_list/', opinions_list, name='opinions_list')
]