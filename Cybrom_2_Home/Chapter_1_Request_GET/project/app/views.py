from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("Hello Home Page")

def new(request):
    name , city = "Vineet" , "Bhopal"
    return render(f'/index/?name={name}&city={city}')

