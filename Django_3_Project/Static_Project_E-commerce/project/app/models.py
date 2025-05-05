from django.db import models

# Create your models here.


class Customer(models.Model):
    cus_name = models.CharField(max_length=60)
    cus_email = models.EmailField(unique=True)
    cus_password = models.CharField(max_length=50) 
    cus_cpassword = models.CharField(max_length=50)
    cus_image = models.ImageField(upload_to='image')
    cus_phone = models.IntegerField()
    cus_location = models.CharField(max_length=50)