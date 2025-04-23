from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    user_email = request.session.get('user_email')
    user_name = request.session.get('user_name')
    # 🟡 Agar user login hai to data bhejo, warna None
    context = {
        'user_email': user_email,
        'user_name': user_name
    }

    return render(request, "comman.html", context)

def mens(request):
    return render(request,"mens.html")

def womenes(request):
    return render(request,"womenes.html")

def kides(request):
    return render(request,"kides.html")

def electranic(request):
    return render(request,"electranic.html")

def grousary(request):
    return render(request,"grousary.html")

def offer(request):
    return render(request,"offer.html")

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")


def signupdata(request):
    print("###########",request.method)
    print("###########",request.POST)
    username = request.POST.get('username')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    password = request.POST.get('password')
    cpassword = request.POST.get('cpassword')
    gender = request.POST.get('gender')

    user = Student.objects.filter(stu_email = email)
    print("$$$$$$$$$$$4 : ",user)
    if user.exists():
        msg = 'user already exits with thise email'
        return render(request,"signup.html",{'msg':msg})

    else:
        if password == cpassword:
            Student.objects.create(
                stu_name = username,
                stu_email = email,
                stu_phone = phone,
                stu_password = password,
                stu_cpassword = cpassword,
                stu_gender = gender
            )
            msg = 'account created sucessfully'
            return render(request,"login.html",{'msg':msg})

        else:
            msg = 'password is not matched hare'
            userdata = {
                'username':username,
                'email':email,
                'phone':phone,
                'password':password,
                'cpassword':cpassword,
                'gender':gender
            }
            return render(request,"signup.html",{'msg':msg,'userdata':userdata})

        


def logindata(request):
    e = request.POST.get('email')
    p = request.POST.get('password')
    print("User Email : ",e," And USer PAssword : ",p)
  
    if request.method == 'POST':
        user = Student.objects.filter(stu_email = e)

        if user.exists():
            userdata = Student.objects.get(stu_email = e)
            storedPass = userdata.stu_password

            if storedPass == p:
                # 🟢 User info session me store karo
                request.session['user_email'] = userdata.stu_email
                request.session['user_name'] = userdata.stu_name
                msg = 'login Succesfully : '
                return render(request,"deshbord.html",{'userdata':userdata,'msg':msg})

            else : 
                msg = 'Incorrect Password'
                return render(request,"login.html",{'userdata':userdata,'msg':msg})

        else:
            msg = 'user not inrolled with thise email'
            return render(request,"signup.html",{'msg':msg})

    else :
        return render(request,"login.html")
    


def logout(request):
    request.session.flush()  # sab session data clear kar deta hai
    return render(request, "login.html", {'msg': 'Logged out successfully'})

