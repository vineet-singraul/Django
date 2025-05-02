from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    city = models.CharField(max_length=50)

    class Meta:
        db_table = 'Student'
        verbose_name = 'Newname' 
        verbose_name_plural = "Student" 