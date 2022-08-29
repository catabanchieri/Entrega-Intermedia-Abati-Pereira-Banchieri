from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),    
    path('products/', include('products.urls')), #se utiliza el include para que se pueda acceder a las urls de products
<<<<<<< HEAD
    path('business/', include('business.urls')),
    path('home/',home, name='home'),
    path('business/',business, name='business'),
     path('users/', include('users.urls')),
]
=======
    path('business/', include('business.urls')),   
]
>>>>>>> main
