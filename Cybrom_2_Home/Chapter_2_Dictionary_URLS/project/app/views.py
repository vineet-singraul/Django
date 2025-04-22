from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello This Is Home Page : </h1>')

def index(request):
    data = [{'name': 'Vineet', 'city': 'Bhopal'}, {'name': 'Visal', 'city': 'Indore'}]
    return render(request, 'index.html', {'key1':data})
