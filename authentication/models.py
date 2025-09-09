from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Department(models.Model):
    name = models.CharField(max_length=50)
    abrev = models.CharField(max_length=5)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="departments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

class City(models.Model):
    name = models.CharField(max_length=50)
    abrev = models.CharField(max_length=5)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="cities")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20, blank=True)
    mobile_phone = models.CharField(max_length=15, unique=True)
    address = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="users", null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)






