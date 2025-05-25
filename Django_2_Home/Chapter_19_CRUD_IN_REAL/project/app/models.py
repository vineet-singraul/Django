from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    image = models.ImageField(upload_to='image')
    city = models.CharField(max_length=70)
    about = models.CharField(max_length=70)
    number = models.IntegerField()