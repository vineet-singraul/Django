from django.db import models # type: ignore

# Create your models here.
class Customer(models.Model):
    cstmer_name = models.CharField(max_length=50)
    cstmer_email = models.EmailField(unique=True)
    cstmer_pass = models.CharField(max_length=50)
    cstmer_cpass = models.CharField(max_length=50)
    cstmer_image = models.ImageField(upload_to='image')
    cstmer_phone = models.IntegerField()
    cstmer_city = models.CharField(max_length=50)