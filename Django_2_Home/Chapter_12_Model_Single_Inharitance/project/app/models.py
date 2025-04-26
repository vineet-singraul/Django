from django.db import models

# Create your models here.

class BasicInfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    class Meta:
        abstract = True

class Emplyee(BasicInfo):
    salary = models.IntegerField()
    designation = models.CharField(max_length=50)

class Student(BasicInfo):
    branch = models.CharField(max_length=50)
