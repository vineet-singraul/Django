from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name = models.CharField(max_length=50,unique=True)
    dep_desci = models.CharField(max_length=200)
    dep_hod = models.CharField(max_length=50)


class Student(models.Model):
    stu_name = models.CharField(max_length=50)
    stu_email = models.EmailField()
    stu_dep = models.ForeignKey(Department,on_delete=models.PROTECT,to_field='dep_name',related_name='depart')
    def __str__(self):
        return self.stu_name