from django.shortcuts import render,redirect
from .models import Customer
# Create your views here.


def home(request):
    return render(request, "comman.html") 

def mens(request):
    return render(request,"mens.html")

def womens(request):
    return render(request,"womens.html")

def kides(request):
    return render(request,"kides.html")

def electranics(request):
    return render(request,"electranics.html")

def grousary(request):
    return render(request,"grousary.html")



def signup(request):
  if request.method == 'POST':  
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    cpaas = request.POST.get('cpaas')
    userImage = request.FILES.get('userImage')
    phoneNumber = request.POST.get('phoneNumber')
    city = request.POST.get('city')
     
    user = Customer.objects.filter(cus_email = email)
    if user.exists():
        userdata = {
        'name': name,
        'email': email,
        'password': password,
        'cpaas': cpaas,
        'phoneNumber': phoneNumber,
        'city': city
      }
        msg = 'Email already exists'
        return render(request, "signup.html", {'msg': msg, 'userdata': userdata})

    else:
        if password == cpaas :
            Customer.objects.create(
              cus_name = name,
              cus_email = email,
              cus_password = password,
              cus_cpassword = cpaas,
              cus_image = userImage,
              cus_phone = phoneNumber,
              cus_location = city
            ) 
            msg = 'Account Successfully created'
            return render(request,"login.html",{'msg':msg})
        else:
             userdata = {
               'name': name,
               'email': email,
               'phoneNumber': phoneNumber,
               'city': city
              }
             msg = 'Password Is Not Match'
             return render(request,"signup.html",{'msg':msg,'userdata':userdata})
  else:
      return render(request,"signup.html")  
  


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = Customer.objects.filter(cus_email = email)
       
        if user.exists():
            userdata = Customer.objects.get(cus_email = email)
            sto_pass = userdata.cus_password

            if password == sto_pass:
                msg = 'password is correct'
                data = {
                    'name':userdata.cus_name,
                    'email':userdata.cus_email,
                    'image':userdata.cus_image
                }
                return render(request,"deshbord.html",{'msg':msg,'data':data})

            else:
                msg = 'password is not match'
                userdata = userdata.cus_email
                return render(request,"login.html",{'msg':msg,'userdata':userdata})

        else :
            msg = 'email not found create account'
            return render(request,"sigmup.html",{'msg':msg})

    else:
        return render(request,"login.html")
    







def home1(request,pk):
    userdata = Customer.objects.get(id=pk)
    return render(request,'home.html',{'userdata':userdata})


def mens1(request,pk):
    userdata = Customer.objects.get(id=pk)
    return render(request,'mens.html',{'userdata':userdata})


def womens1(request,pk):
    userdata = Customer.objects.get(id=pk)
    return render(request,'womens.html',{'userdata':userdata})


def kides1(request,pk):
    userdata = Customer.objects.get(id=pk)
    return render(request,'kides.html',{'userdata':userdata})


def electranics1(request,pk):
    userdata = Customer.objects.get(id=pk)
    return render(request,'electranics.html',{'userdata':userdata})



def grousary1(request,pk):
    userdata = Customer.objects.get(id=pk)
    return render(request,'grousary.html',{'userdata':userdata})
