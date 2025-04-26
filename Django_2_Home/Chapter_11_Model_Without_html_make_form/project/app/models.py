from django.db import models  # type: ignore 

# Create your models here.


class BasicInfo(models.Model):
    quali = [("1","B-tech"),("2","M-tech"),("3","P-hd"),("4","Diploma")]
    username = models.CharField(max_length=50,null=True,unique=True,db_index=True,blank=False,help_text="Enter a unique username")
    email = models.EmailField(max_length=255, unique=True, blank=False, db_index=True)
    bio = models.CharField(max_length=50, blank=True, null=True,db_index=True,help_text="Write a short bio about yourself")
    is_active = models.BooleanField(default=False,db_index=True)
    Qualification=models.CharField(max_length=100, choices=quali,null=True,verbose_name='Quali',db_index=True)

    def __str__(self):
        return self.username