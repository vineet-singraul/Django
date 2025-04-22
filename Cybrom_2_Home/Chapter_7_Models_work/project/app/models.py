from django.db import models

# Create your models here.


class Student(models.Model):
    stu_name = models.CharField(max_length=60)
    stu_email = models.EmailField()
    stu_detail = models.CharField(max_length=200)
    stu_phone = models.IntegerField()
    stu_dob = models.DateField()
    stu_image = models.ImageField(upload_to='image')
    stu_file = models.FileField(upload_to='image')
    stu_gender = models.CharField(max_length=50)
    stu_quali = models.CharField(max_length=60)
    stu_pass = models.CharField(max_length=60)
