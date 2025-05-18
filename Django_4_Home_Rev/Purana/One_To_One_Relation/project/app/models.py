from django.db import models

# Create your models here.

class Aadhar(models.Model):
    aadhar_no = models.IntegerField(unique=True)
    created_by = models.CharField(max_length=50)
    def __str__(self):
        return str(self.aadhar_no)


class Student(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    email = models.EmailField()
    aadhar_user = models.OneToOneField(Aadhar,on_delete=models.PROTECT,to_field='aadhar_no')
    def __str__(self):
        return self.name