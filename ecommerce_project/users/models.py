from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=40)
    surname= models.CharField(max_length=40)
    birth_date= models.DateField()
    address= models.CharField(max_length=40)
    
    #avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    