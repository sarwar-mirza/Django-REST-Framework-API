from django.db import models

# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=(('Male', 'Male'), ('Female', 'Female')))
    
    def __str__(self):
        return self.name
    
    
    
class Songs(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='gaan')
    duration = models.IntegerField()
    
    def __str__(self):
        return self.title
    
    
    
