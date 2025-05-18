from django.shortcuts import render
from .models import Student,Department
# Create your views here.


def student(request):
    data = Student.objects.all()
    print("**********")
    print(data)
    print(data.values())
    print(data.values_list())

    data1 = Student.objects.get(stu_name='Vineet')
    print("#######################")
    print(data1.id)
    print(data1.stu_name)
    print(data1.stu_email)
    print(data1.sty_city)
    # data forword access  from table
    print(data1.stu_department.department_name)
    print(data1.stu_department.department_hod)



def department(request):
    print("***************")
    data = Department.objects.all()
    print(data)
    print(data.values())
    print(data.values_list())

    dep_data = Department.objects.get(id=2)
    print(dep_data.id)
    print(dep_data.department_name)
    print(dep_data.department_hod)

    print("Reverse data access")
    print(dep_data.depart.all().count())