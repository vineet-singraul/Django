from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello Thise Is Home Page</h1>")

def about(request):
    data = {'name':True , 'age':False , 'quali':None}
    return JsonResponse(data)

# def index(request):
#     return render(request , 'index.html')



# multiple user data send
# def index(request):
#     data = [{'name':'Vineet' , 'city':'bhopal'} , {'name':'Anmol' , 'city':'indore'}]
#     return render(request ,  'index.html' , {'key1':data})


# single data send
# def index(request):
#     data = {'name':'Vineet' , 'city':'bhopal'}
#     return render(request ,  'index.html' , data)


def index(request):
    x = { }
    data = {'name':'Vineet' , 'city':'bhopal'}
    x['key1'] = data
    return render(request ,  'index.html' , x)


def new(request):
    return redirect('https://dsa-delta-eight.vercel.app/')