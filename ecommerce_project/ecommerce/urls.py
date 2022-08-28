from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),    
    path('products/', include('products.urls')), #se utiliza el include para que se pueda acceder a las urls de products
    path('business/', include('business.urls')),   
]