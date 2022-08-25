from django.contrib import admin
from django.urls import path, include
from home.views import home
from business.views import business

urlpatterns = [
    path('',home, name='home'), # home page
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')), #se utiliza el include para que se pueda acceder a las urls de products
    path('business/', include('business.urls')),    
    path('business/',business, name='business')
]
