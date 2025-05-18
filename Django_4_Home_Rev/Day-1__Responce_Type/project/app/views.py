from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect,render
# Create your views here.


def home(request):
    return HttpResponse("<h1>Hello</h1>")

def about(request):
    data = {'name':True,'age':False,'quali':None}
    return JsonResponse(data)

def contect(request):
    data = {'name':'Vineet','age':21,'city':'Bhopal'}
    return render(request,'index.html',{'data':data})

def new(request):
    return redirect('https://www.google.com/')