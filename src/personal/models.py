from django.db import models

# Create your models here.
class personal(models.Model):
        first_name = models.CharField(max_length=60, help_text='Their first name')
        last_name = models.CharField(max_length=80, blank=True, help_text='Do you know it?')
        birtday = models.DateField()