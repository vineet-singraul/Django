from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "comman.html")

def about(request):
    return render(request, "about.html")

def content(request):
    return render(request , "content.html")

def ragister(request):
    return render(request , "ragister.html")

def login(request):
    return render(request , "login.html")

def registerdata(request):
    return render(request , "registerdata.html")