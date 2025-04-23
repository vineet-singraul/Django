from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    data = {'name':'vineet'}
    return render(request,"comman.html",{'data':data})

def about(request):
    return render(request,"about.html")

def contect(request):
    return render(request,"contect.html")

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")


def registerdata(request):
    print("***********", request.method)
    print("***********", request.POST)

    username = request.POST.get('username')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    dob = request.POST.get('dob')
    password = request.POST.get('password')
    cpassword = request.POST.get('cpassword')
    gender = request.POST.get('gender')
    subscribe = request.POST.getlist('subscribe')
    detail = request.POST.get('detail')
    image = request.FILES.get('profile-pic')
    resume = request.FILES.get('resume')

    user = Student.objects.filter(stu_email=email)
    if user.exists():
        msg = 'User already exists with this email'
        return render(request, "register.html", {'msg': msg})
    else:
        if password == cpassword:
            Student.objects.create(
                   stu_name=username,
                   stu_email=email,
                   stu_phone=phone,
                   stu_dob=dob,
                   stu_password=password,
                   stu_cpassword=cpassword, 
                   stu_gender=gender,
                   stu_subscribe=subscribe,
                   stu_detail=detail,
                   stu_image=image,
                   stu_resume=resume
            )
            msg = 'Registration Successful!'
            return render(request, "login.html", {'msg': msg})
        else:
            msg = 'Password Is Not Matched !'
            return render(request,"register.html",{'msg':msg})
