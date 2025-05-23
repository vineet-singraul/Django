from django.db import models

class CEO(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CarCompany(models.Model):
    name = models.CharField(max_length=100)
    ceo = models.OneToOneField(CEO, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
