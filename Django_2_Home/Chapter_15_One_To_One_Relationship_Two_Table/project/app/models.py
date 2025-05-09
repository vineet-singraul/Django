from django.db import models

# Create your models here.

class department(models.Model):
    deprtmnt = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.deprtmnt

class student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    department_name = models.OneToOneField(department,on_delete=models.PROTECT,to_field='deprtmnt')

    def __str__(self):
        return self.name