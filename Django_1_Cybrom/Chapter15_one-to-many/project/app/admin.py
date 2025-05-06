from django.contrib import admin
from .models import Aadhar,User
from .models import Department,Student,Fule,Vehicles
# Register your models here.

admin.site.register(Aadhar)
admin.site.register(User)

admin.site.register(Department)
admin.site.register(Student)


admin.site.register(Fule)
admin.site.register(Vehicles)