from django.shortcuts import render
from .models import Student,Aadhar


def student(request):
    data = Student.objects.all()
    print("***************")
    print(data)
    print(data.values())
    print(data.values_list())

#     data1 = Student.objects.get(name='Anmol')
#     print(data1.id)

def aadhar(request):
    aadhar_data = Aadhar.objects.get(aadhar_no=1234)
    print(aadhar_data.student.name)
    print(aadhar_data.student.email)
    print(aadhar_data.student.city)
    print(aadhar_data.aadhar_no)
    print(aadhar_data.created_by)