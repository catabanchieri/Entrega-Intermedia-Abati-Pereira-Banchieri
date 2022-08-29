from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),    
    path('products/', include('products.urls')),
    path('business/', include('business.urls')),
    path('users/', include('users.urls')),
]
