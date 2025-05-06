from django.shortcuts import render
from .models import User,Department
# Create your views here.

def Student(request):
    data = User.objects.all()
    print(data)
    print(data.values)
    print(data.values_list())

    data1 = User.objects.get(name = "Vineet Singraul")

    print(data1.name)
    print(data1.email)
    print(data1.contect)
    print(data1.roll)
    # print(data1.aadhar_no)
    print(data1.aadhar_no.aadhar)
    print(data1.aadhar_no.created_by)




def department(request):
    data = Department.objects.all()
    print(data)
    print(data.values())
    print(data.values_list())

    dep_data = Department.objects.get(id=1)
    print(dep_data.id)
    print(dep_data.dep_name)
    print(dep_data.dep_des)
    print(dep_data.dep_hod)

    print(dep_data.depart.all().count())
    x = dep_data.depart.all()
    print(x)



