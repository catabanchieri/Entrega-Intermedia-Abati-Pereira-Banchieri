from django.db import models


class Stores(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone_number = models.IntegerField()
    schedules = models.CharField(max_length=100)

