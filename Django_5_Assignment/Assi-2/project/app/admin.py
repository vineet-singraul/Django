from django.contrib import admin
from .models import CarCompany,CarModel
# Register your models here.


admin.site.register(CarCompany)
admin.site.register(CarModel)









# from yourapp.models import CarCompany, CarModel

# # Add Company
# bmw = CarCompany.objects.create(name="BMW")

# # Add CarModel
# CarModel.objects.create(name="X1", company=bmw)
# CarModel.objects.create(name="X3", company=bmw)

# # Retrieve CarModels by company
# for model in bmw.models.all():
#     print(model.name)
