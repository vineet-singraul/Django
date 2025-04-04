from django.shortcuts import render,redirect
from django.http import HttpResponse , JsonResponse

# Create your views here.

def home(request):
    x = "<h1>Hello...</h1>"
    return HttpResponse(x)

def about(request):
   data = {'name':True , 'age':False , 'quali':None}
   return JsonResponse(data)

def index(request):
    return render(request , 'index.html')


def new(request):
    return redirect('https://dsa-delta-eight.vercel.app/')
