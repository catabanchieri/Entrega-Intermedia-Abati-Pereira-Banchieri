from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, related_name='profile')
    name= models.CharField(max_length=40)
    surname= models.CharField(max_length=40 )
    email=models.EmailField(max_length=40,default='@gmail.com')
    birth_date= models.DateField()
    phone_number= models.IntegerField(default='00000')
    address= models.CharField(max_length=40 )

    def __str__(self):
        return self.user.username
    
    #avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    