from django.db import models

# Create your models here.
class User(models.Model):
    
    name = models.CharField(max_length=50)
    score = models.IntegerField()
    
    def __str__(self):
        return self.name