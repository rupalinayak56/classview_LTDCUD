from django.db import models
from django.urls import reverse 
# Create your models here.
class School(models.Model):
    ScName=models.CharField(max_length=100)
    ScPrincipal=models.CharField(max_length=100)
    ScLocation=models.CharField(max_length=100)

    def __str__(self):
        return self.ScName

    def get_absolute_url(self):
        return reverse('SchoolDetails',kwargs={'pk':self.pk})

class Student(models.Model):
    Sname=models.CharField(max_length=100)
    Sage=models.IntegerField()
    Scname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')


    def __str__(self):
        return self.Sname
