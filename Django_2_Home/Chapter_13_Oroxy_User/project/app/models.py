from django.db import models

# Create your models here.

class MainModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contect = models.IntegerField()
    addBy = models.CharField(max_length=50)


class ProxyModel(MainModel):
    class Meta:
        proxy = True