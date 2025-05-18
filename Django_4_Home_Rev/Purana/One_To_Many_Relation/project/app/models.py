from django.db import models
# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=50,unique=True)
    department_hod = models.CharField(max_length=50)
    def __str__(self):
        return self.department_name
    

class Student(models.Model):
    stu_name = models.CharField(max_length=50)
    stu_email = models.EmailField()
    sty_city = models.CharField(max_length=60)
    stu_department = models.ForeignKey(Department,on_delete=models.PROTECT,to_field='department_name',related_name='depart')
    def __str__(self):
        return self.stu_name