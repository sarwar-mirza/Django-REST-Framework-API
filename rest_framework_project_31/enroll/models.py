from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    department = models.CharField(max_length=50)
    city = models.CharField(max_length=40)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=50)
    



    
    
