from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def Home(request):
    return HttpResponse('<h1>Hello Vineet </h1>')


