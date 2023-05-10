from django.db import models

# Create your models here.

class homepage(models.Model):
    Title = models.CharField(max_length=50)
    AboutMe = models.TextField(max_length=500)
    Aim = models.TextField(max_length=500)
    Background = models.TextField(max_length=500)
    Approach= models.TextField(max_length=500)