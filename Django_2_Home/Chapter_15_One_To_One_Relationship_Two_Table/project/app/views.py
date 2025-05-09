from django.shortcuts import render
from .models import student
# Create your views here.

def Student(request):
    data = student.objects.all()
    print(data)