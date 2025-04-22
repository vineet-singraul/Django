from django.shortcuts import render
from .models import Student
# Create your views here.


def home(request):
    data = {'name':'vineet'}
    return render(request , "comman.html" , {'data':data})

def about(request):
    return render(request , "about.html")

def contect(request):
    return render(request , "contect.html")

def ragister(request):
    return render(request , "ragister.html")

def login(request):
    return render(request , "login.html")

def ragisterdata(request):
    print("==================",request.method)
    print("==================",request.POST)
    username = request.POST.get('username')
    email = request.POST.get('email')
    detail = request.POST.get('detail')
    phone = request.POST.get('phone')
    gender = request.POST.get('gender')
    subscribe = request.POST.getlist('subscribe')
    dob = request.POST.get('dob')
    image = request.POST.get('profile-pic')
    resume = request.POST.get('resume')
    password = request.POST.get('password')
    # print("Name IS : ",username)
    # print("email IS : ",email)
    # print("detail IS : ",detail)
    # print("phone IS : ",phone)
    # print("dob IS : ",dob)
    # print("password IS : ",password)

    Student.objects.create(stu_name=username,
                           stu_email=email,
                           stu_detail=detail,
                           stu_phone=phone,
                           stu_dob=dob,
                           stu_gender=gender,
                           stu_quali=subscribe,
                           stu_pass=password)
