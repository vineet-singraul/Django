from django.db import models

# Create your models here.

class Aadhar(models.Model):
    aadhar = models.IntegerField(unique=True)
    created_by = models.CharField(max_length=50)
   
    def __str__(self):
        return str(self.aadhar)

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contect = models.IntegerField()
    roll = models.IntegerField()
    aadhar_no = models.OneToOneField(Aadhar,on_delete=models.PROTECT,to_field="aadhar")

    def __str__(self):
        return self.name