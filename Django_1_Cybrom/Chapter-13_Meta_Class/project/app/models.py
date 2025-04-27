from django.db import models

# Create your models here.
class  Student(models.Model):
    stu_name = models.CharField(max_length=50)
    stu_email = models.EmailField()
    stu_contect = models.CharField(max_length=50)
    stu_city = models.CharField(max_length=50)

    class Meta:
        db_table = 'Student'   # change table name using thise
        verbose_name = 'NewName'  # change table name in admin panel
        verbose_name_plural = "Student"  # remove the last s from class


        # ordering = ['id']
        # ordering = ['-id']
        ordering = ['-stu_name']
