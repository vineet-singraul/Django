from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
# Create your views here.

def home(request):
    return HttpResponse('<h1>Thise Is Home Page : <h1\>')

def about(request):
    data = {'name':True , 'age':False , 'quali':None}
    return JsonResponse(data)

# def index(request):
#     return render(request ,  'index.html')

def index(request):
    data = [{'name':'Vineet' , 'city':'Satna'},{'name':'anmol' , 'city':'Bhopal'}]
    return render(request ,  'index.html' , {'key1' : data})

def new(request):
    return redirect('https:www.google.com')