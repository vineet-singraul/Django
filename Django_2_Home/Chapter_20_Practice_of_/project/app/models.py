from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    gender = models.CharField(max_length=70)
    image = models.ImageField(upload_to='image')
    number = models.IntegerField()
    email = models.EmailField()