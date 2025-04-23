from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request , "comman.html")

def about(request):
    return render(request , "about.html")

def contect(request):
    return render(request , "contect.html")

def login(request):
    return render(request , "login.html")

def ragister(request):
    return render(request , "ragister.html")

def ragisterdata(request):
    # return render(request , "ragisterdata.html")
    print(" +++++++++++++++++++ ",request.GET)  
    # print("GET DATA HAI YE --- : ",request.method)
    # print("-----------------")
    # print("Posted Data Hai YE : ",request.POST)
    # print("-----------------")
    # username = request.GET.get('username')
    # email = request.POST.get('email')
    # detail = request.POST.get('detail')
    # phone = request.POST.get('phone')
    # dob = request.POST.get('dob')
    # subscribe = request.POST.getlist('subscribe')
    # password = request.POST.get('password')
    # cpassword = request.POST.get('cpassword')
    # print("User Name : ",username)
    # print("User Email; : ",email)
    # print("User detail; : ",detail)
    # print("User phone; : ",phone)
    # print("User dob; : ",dob)
    # print("User subscribe; : ",subscribe)
    # print("User password; : ",password)
    # print("User cpassword; : ",cpassword)
