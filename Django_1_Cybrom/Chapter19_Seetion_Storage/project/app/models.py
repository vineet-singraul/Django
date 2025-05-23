from django.db import models

# Create your models here.

class Item(models.Model):
    item_name=models.CharField(max_length=30)
    item_des=models.CharField(max_length=20)
    item_price=models.IntegerField()
    item_quantity=models.IntegerField()