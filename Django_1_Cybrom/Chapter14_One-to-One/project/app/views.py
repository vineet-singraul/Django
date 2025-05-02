from django.shortcuts import render
from .models import User
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