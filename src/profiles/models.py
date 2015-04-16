from django.db import models

# Create your models here.
class profile(models.Model):
    name=models.CharField(max_length=1200)
    empid=models.CharField(max_length=15,default='My EmpID')
    designation=models.CharField(max_length=1200,default='My Designation')
    location=models.CharField(max_length=1200,default='My Location')
    join_date = models.DateTimeField()

    def __unicode__(self):
        return self.name