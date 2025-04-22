from django.shortcuts import render

# Create your views here.

def home(request):
    data = {'name':'','age':21}
    return render(request , "comman.html" , {'data':data})

def about(request):
    return render(request , "about.html")

def contect(request):
    return render(request , "contect.html")

def login(request):
    return render(request , "login.html")

def ragister(request):
    return render(request , "ragister.html")
