from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello Vineet Home Page : <h1/>')

def about(request):
    data = {"name":True , "City":False , "Quali":None}
    return JsonResponse(data)

def index(request):
    return render(request , 'index.html')

def urlPage(request):
    return redirect('https://www.google.com/')