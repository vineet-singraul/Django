from django.db import models

class CarCompany(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(CarCompany, on_delete=models.CASCADE, related_name='models')

    def __str__(self):
        return self.name
