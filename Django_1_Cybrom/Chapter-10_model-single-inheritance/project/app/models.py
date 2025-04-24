from django.db import models

# Create your models here.

class Baseinfo(models.Model):
    name =models.CharField(max_length=60)
    email = models.EmailField()
    contect = models.IntegerField()
    class Meta:
        abstract = True

class Student(Baseinfo):
     branch = models.CharField(max_length=50)

class Employee(Baseinfo):
    department = models.CharField(max_length=100)
    salary = models.IntegerField()
    def __str__(self):
        return self.name

class Client(Baseinfo):
    project = models.CharField(max_length=200)
    def __str__(self):
        return self.name