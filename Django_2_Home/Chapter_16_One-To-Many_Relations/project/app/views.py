from django.shortcuts import render
from .models import Student,Department
# Create your views here.
def student(request):
    data = Student.objects.all()
    print(data)
    print(data.values())
    print(data.values_list())

    stu_data = Student.objects.get(stu_name='Vineet')
    print("#############",stu_data)
    print(stu_data.id)
    print(stu_data.stu_name)
    print(stu_data.stu_email)
    print(stu_data.stu_dep)
    print("*********")
    print(stu_data.stu_dep.dep_name)
    print(stu_data.stu_dep.dep_hod)
    print(stu_data.stu_dep.dep_desci)