from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100),
    secondName = models.CharField(max_length=100),
    phone = models.CharField(max_length=100),
    dni = models.CharField(max_length=100),
    email = models.CharField(max_length=100),
    address = models.CharField(max_length=100)
