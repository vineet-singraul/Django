from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    return render(request,'home.html')

def first(request):
    single = 'single'
    data = Student.objects.first()
    return render(request,'home.html',{'data':data,'single':single})

def last(request):
    single = 'single'
    data = Student.objects.last()
    return render(request,'home.html',{'data':data,'single':single})


def firstfive(request):
    data = Student.objects.all()[:5]
    return render(request,'home.html',{'data':data})


def lastfive(request):
    data = Student.objects.order_by('-id')[:5]
    return render(request, 'home.html', {'data': data})


def accending(request):
    data = Student.objects.order_by('name')
    return render(request, 'home.html', {'data': data})


def deaccending(request):
    data = Student.objects.order_by('-id')
    return render(request, 'home.html', {'data': data})