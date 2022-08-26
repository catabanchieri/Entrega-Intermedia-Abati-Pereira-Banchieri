from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')), #se utiliza el include para que se pueda acceder a las urls de products
    path('articles/', include('blog.urls')), 
    path('business/', include('business.urls')),
    path('home/', include('home.urls')),
]
