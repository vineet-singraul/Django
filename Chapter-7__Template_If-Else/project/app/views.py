from django.shortcuts import render

# Create your views here.


def landing(request):
    return render(request,'home.html')

def home(request):
    data = {
        'name':'vineet',
        'age':21,
        'city':'bhopal'
    }
    return render(request,'home.html',{'data':data})