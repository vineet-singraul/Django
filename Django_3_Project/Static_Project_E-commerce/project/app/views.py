from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"comman.html")

def mens(request):
    return render(request,"mens.html")

def womens(request):
    return render(request,"womens.html")

def kides(request):
    return render(request,"kides.html")

def electranics(request):
    return render(request,"electranics.html")

def grousary(request):
    return render(request,"grousary.html")

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")