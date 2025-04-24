from django.db import models

# Create your models here.
class BaseInfo(models.Model):
        name = models.CharField(max_length=50)
        email = models.EmailField()
        contect = models.IntegerField()

class Student(BaseInfo):
        branch = models.CharField(max_length=40)
        fees = models.IntegerField()

    
class Emplyee(BaseInfo):
        department = models.CharField(max_length=30)
        salary = models.IntegerField()



class MainModel(models.Model):
        name = models.CharField(max_length=20)
        email = models.EmailField()
        contect = models.IntegerField()
        add = models.CharField(max_length=20)

class ProxyModel(models.Model):
        class Meta:
            proxy = True