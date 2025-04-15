from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    return render(request , 'home.html')

def about(request):
    return render(request , 'about.html')

def contact(request):
    return render(request , 'contact.html')

def register(request):
    return render(request , 'register.html')


def login(request):
    return render(request , 'login.html')


def registerdata(request):
    print(request.method)
    print(request.POST)
    # print(request.GET)
    # print(request.FILES)
    # print(request.COOKIES)
    # print(request.META)
    username = request.POST.get('username')
    email = request.POST.get('email')
    detail = request.POST.get('detail')
    phone = request.POST.get('phone')
    dob = request.POST.get('dob')
    subscribe = request.POST.getlist('subscribe')
    gender = request.POST.get('gender')
    password = request.POST.get('password')
    cpassword = request.POST.get('cpassword')
    image = request.FILES.get('profile-pic')
    document = request.FILES.get('resume')
    print(username,email,detail,phone,dob,subscribe,gender,password,cpassword)

    Student.objects.create(stu_name=username,
                            stu_email=email,
                            stu_dis = detail , 
                            stu_contect = phone,
                            stu_dob = dob,
                            stu_quali = subscribe , 
                            stu_gender = gender)

