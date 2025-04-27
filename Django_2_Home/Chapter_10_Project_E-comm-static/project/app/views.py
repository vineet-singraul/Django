from django.shortcuts import render # type: ignore
from .models import Customer
# Create your views here.

def home(request):
    n = request.POST.get('name')
    user = Customer.objects.get(cstmer_name = n)
    return render(request,"comman.html")

def mens(request):
    return render(request,"mens.html")

def womens(request):
    return render(request,"womens.html")

def kides(request):
    return render(request,"kides.html")

def electranic(request):
    return render(request,"electranic.html")

def grousary(request):
    return render(request,"grousary.html")

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")



def signupdata(request):
        print(request.method)
        print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpaas = request.POST.get('cpaas')
        userImage = request.FILES.get('userImage')
        phone = request.POST.get('phoneNumber')
        city = request.POST.get('city')
        print("######################")

        user = Customer.objects.filter(cstmer_email = email)

        if user.exists():
            msg = 'email already exits hare signup again'
            return render(request,"signup.html",{'msg':msg})
        else:
            if password == cpaas:   
                Customer.objects.create(
                    cstmer_name = name,
                    cstmer_email = email,
                    cstmer_pass = password,
                    cstmer_cpass = cpaas,
                    cstmer_image = userImage,
                    cstmer_phone = phone,
                    cstmer_city = city
                )
                msg = 'Succesfully Ragistered user :'
                return render(request,"login.html",{'msg':msg})
            
            else:
                 msg = 'Password not matched try again'
                 userdata = {
                  'cstmer_name': name,
                  'cstmer_email': email,
                  'cstmer_phone': phone,
                  'cstmer_city': city
                 }
                 return render(request, "signup.html", {'msg': msg, 'userdata': userdata})





def logindata(request):
     
    if request.method == 'POST':
            userEmail = request.POST.get('email')
            userPass = request.POST.get('password')
            user = Customer.objects.filter(cstmer_email = userEmail)
            if user.exists():
                userdata = Customer.objects.get(cstmer_email = userEmail)
                storePass = userdata.cstmer_cpass

                if storePass == userPass:
                     msg = 'Password Matched'
                     return render(request,"deshbord.html",{'msg':msg,'userdata':userdata})

                else:
                    msg = 'Password does not match.'
                    autoFillData = {
                    'cstmer_email': userEmail
                    }
                    return render(request, "login.html", {'msg': msg, 'autoFillData': autoFillData})

            else:
                 msg = 'Email Not Found Ragistred Account'
                 return render(request,"signup.html",{'msg':msg})

    return render(request,"login.html")