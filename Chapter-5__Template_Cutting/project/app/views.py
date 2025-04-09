from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request , 'home.html')

def about(request):
    return render(request , 'about.html')

def contact(request):
    return render(request , 'contact.html')

def register(request):
    return render(request , 'register.html')

def registerdata(request):
    print(request.method)
    print(request.POST)
    print(request.GET)
    print(request.FILES)
    print(request.COOKIES)
    print(request.META)

def login(request):
    return render(request , 'login.html')