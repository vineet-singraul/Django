from django.db import models

# Create your models here.
class Student(models.Model):
    stu_name = models.CharField(max_length=50)
    stu_email = models.EmailField(unique=True)
    stu_detail = models.CharField(max_length=200)
    stu_phone = models.IntegerField()
    stu_dob = models.DateField()
    stu_quali = models.CharField(max_length=50)
    stu_gender = models.CharField(max_length=50)
    stu_image = models.ImageField(upload_to='image')
    stu_resume = models.FileField(upload_to='image')
    stu_pass = models.CharField(max_length=50)

