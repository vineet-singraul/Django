from django.shortcuts import render # type: ignore

def home(request):
    data = {'name':'vineet','age':21,'quali':'B-tech'}
    return render(request , "comman.html", {'data':data})

def about(request):
    data = {'name':'vineet','age':21,'quali':'B-tech'}
    return render(request , "about.html",{'data':data})

def contect(request):
    return render(request , "contect.html")

def login(request):
    return render(request , "login.html")

def ragister(request):
    return render(request , "ragister.html")

def ragisterdata(request):
    return render(request , "ragisterdata.html")