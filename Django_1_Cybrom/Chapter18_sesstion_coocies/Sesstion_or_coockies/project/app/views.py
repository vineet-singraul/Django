from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'app/register.html')

def register(request):
    print(request.METHOD)