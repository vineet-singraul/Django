from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    name = {'name':'vineet'}
    return render(request, 'comman.html')


def about(request):
    return render(request,'about.html')

def contect(request):
    return render(request,'contect.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def signupdata(request):
    # print("#############",request.method)
    # print("#############",request.POST)
    username = request.POST.get('username')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    password = request.POST.get('password')
    cpassword = request.POST.get('cpassword')
    gender = request.POST.get('gender')

    user = Student.objects.filter(stu_email = email)
    if user.exists():
       msg = 'email alrady exists'
       return render(request,"signup.html",{'msg':msg})
    else:
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password == cpassword:
            Student.objects.create(
                stu_name = username,
                stu_email = email,
                stu_phone = phone,
                stu_password = password,
                stu_cpassword = cpassword,
                stu_gender = gender
            )
            msg = 'Account Sucsessfully Created'
            return render(request,"login.html",{'msg':msg})    
        else:
            msg = 'Password not match '
            return render(request,"signup.html",{'msg':msg})

def logindata(request):
    if request.method == 'POST':
        e = request.POST.get('email')
        p = request.POST.get('password')
        user = Student.objects.filter(stu_email = e)

        if user:
            userdata = Student.objects.get(stu_email = e)
            p1 = userdata.stu_password

            if p==p1:
                msg = 'Password Is Matched :'
                return render(request,'dashbord.html',{'msg':msg})

            else:
                msg = 'Password Is Not Matched'
                return render(request,"login.html",{'msg':msg,'email':e})
        else:
            msg = 'Email Not Exits :'
            return render(request,"signup.html",{'msg':msg})
    else:
        return render(request,"login.html")
    


              
    
              
      
      
  
