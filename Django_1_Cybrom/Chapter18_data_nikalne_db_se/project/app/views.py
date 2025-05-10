from django.shortcuts import render
from .models import Student
# Create your views here.

def index(request):
    return render(request,'index.html')

def first(request):
    data = Student.objects.first()
    return render(request,'index.html',{'data':data})