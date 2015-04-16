from django.db import models
from django.contrib import admin
# Create your models here.
from django.db import models

class PersonTest(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    age = models.IntegerField()

