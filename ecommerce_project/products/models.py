from django.db import models

#debemos crear 3 clases para los productos

class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=200, null=True, blank=True)
    stock = models.IntegerField()
    size = models.CharField(max_length=5) # S, M, L, XL, XXL
    #image = models.ImageField(upload_to='images/', null=True, blank=True)