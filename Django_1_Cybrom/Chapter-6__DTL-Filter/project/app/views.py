from django.shortcuts import render

# Create your views here.


def home(request):
    data = {'age':21 , 'quali':'devloper'}

    return render(request , 'home.html' , data)