from django.db import models

# Create your models here.

class Student (models.Model):
    stu_name = models.CharField(max_length=50)
    stu_email = models.EmailField()
    stu_dis = models.CharField(max_length=200)
    stu_contect = models.IntegerField()
    stu_dob = models.DateField()
    stu_quali = models.CharField(max_length=50)
    stu_gender = models.CharField(max_length=50)
    stu_image = models.ImageField(upload_to='image')
    stu_document = models.FileField(upload_to='image')
    stu_password = models.CharField(max_length=15)

    