from django.shortcuts import render
from .models import Student
# Create your views here.


def home(request):
    # all_data = Student.objects.all()
    # print(all_data)
    # print("***********",all_data.values_list())    # data list form me print hoga
    data = Student.objects.filter(name='vineet',city='Bhopal')
    print(data)
    print(data.values())
    print(data.values_list())