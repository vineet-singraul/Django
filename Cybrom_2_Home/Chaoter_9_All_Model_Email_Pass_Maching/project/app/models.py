from django.db import models

# Create your models here.

class Student(models.Model):
    stu_name = models.CharField(max_length=50)
    stu_email = models.EmailField(unique=True)
    stu_phone = models.IntegerField()
    stu_dob = models.DateField()
    stu_password = models.CharField(max_length=50)
    stu_cpassword = models.CharField(max_length=50)
    stu_gender = models.CharField(max_length=60)
    stu_subscribe = models.CharField(max_length=60)
    stu_detail = models.CharField(max_length=60)
    stu_image = models.ImageField(upload_to='image')
    stu_resume = models.FileField(upload_to='image')