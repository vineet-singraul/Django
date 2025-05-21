from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'comman.html')

def about(request):
    return render(request,'about.html')

def contect(request):
    return render(request,'contect.html')

def signup(request):
    return render(request,'signup.html')

def login(request):
    userdata = {'name':'vineet'}
    return render(request,'login.html',{'userdata':userdata})

def logout(request):
    return render(request,'home.html')