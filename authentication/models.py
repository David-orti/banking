from django.db import models

# Create your models here.
class   User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=150)
     
     
class Country(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10)










