from django.db import models
from django.contrib import admin
from datetime import date
# Create your models here.
from django.db import models

class PersonTest(models.Model):
    name = models.CharField(max_length=200)
    Empid = models.CharField(max_length=200,default='SampleEmpid')
    designation = models.CharField(max_length=200,null=True)
    department = models.CharField(max_length=200,null=True)
    dob = models.DateField(("Date"), auto_now_add = True)
    Address = models.TextField(null=True)
    Mobile = models.CharField(max_length=15)
    EmgContact = models.CharField(max_length=15,null=True)
    bloodgroup = models.CharField(max_length=15,null=True)
    email = models.EmailField(max_length=45,null=True)

