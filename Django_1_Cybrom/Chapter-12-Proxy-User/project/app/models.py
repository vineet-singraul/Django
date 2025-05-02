from django.db import models

# Create your models here.

class Mainmodel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contect = models.CharField(max_length=40)
    add = models.CharField(max_length=40)


class ProxyModel(Mainmodel):
    class Meta:
        proxy = True  