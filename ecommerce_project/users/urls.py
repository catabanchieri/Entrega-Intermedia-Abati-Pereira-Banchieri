
from django.urls import path
from users.views import login_request,register ,create_profile,user_profile,update_profile,delete_profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
path('login/',login_request,name='login'),
path('register/',register,name='register'),
path('logout/', LogoutView.as_view(template_name='users/logout.html'),name='logout'),
path('create_profile/',create_profile,name='create-profile'),
path('user_profile/',user_profile,name='user-profile'),
path('update_profile/',update_profile,name='update-profile'),
path('delete_profile/',delete_profile,name='delete-profile')
]


