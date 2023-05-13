from django.db import models

# Create your models here.

class homepage(models.Model):
    Title = models.CharField(max_length=50)
    AboutMe = models.TextField(max_length=800)
    Aim = models.TextField(max_length=800)
    Background = models.TextField(max_length=800)
    Approach= models.TextField(max_length=800)
