from django.shortcuts import render,redirect
from .models import Customer,Query
from django.db.models import Q
# Create your views here.


def home(request):
    return render(request, "home.html") 

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
                return render(request,"deshbord.html",{'msg':msg,'userdata':userdata})

            else:
                msg = 'password is not match'
                return render(request,"login.html",{'msg':msg,'userdata':userdata})

        else :
            msg = 'email not found create account'
            return render(request,"signup.html",{'msg':msg})

    else:
        return render(request,"login.html")
    







def home1(request,pk):
    print("################")
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


def deshbord(request, pk):
    try:
        userdata = Customer.objects.get(id=pk)
    except Customer.DoesNotExist:
        return redirect('login')  # Redirect to login if user does not exist

    return render(request, "deshbord.html", {'userdata': userdata})



# Query ke liye functions
def query(request, pk):
    user = Customer.objects.get(id=pk)
    userdata = {
        "id": user.id,
        "cus_name": user.cus_name,
        "cus_email": user.cus_email,
        "cus_email": user.cus_email,
        "cus_image": user.cus_image,
        "cus_phone": user.cus_phone,
    }
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        query = request.POST.get('query')
        Query.objects.create(
            cus_name_q=name,
            cus_email_q=email,
            cus_query_q=query
        )
        querydetail = Query.objects.filter(cus_email_q=email)
        return render(request, 'deshbord.html', {'userdata': userdata, 'querydetail': querydetail})
    else:
        return render(request, 'deshbord.html', {'userdata': userdata, 'query': userdata})



def allquery(request,pk):
    print(pk)
    userdata = Customer.objects.get(id=pk)
    print(userdata.cus_email)
    x= userdata.cus_email
    userdata={
        "id":userdata.id,
        "cus_name": userdata.cus_name,
        "cus_email": userdata.cus_email,
        "cus_email": userdata.cus_email,
        "cus_image": userdata.cus_image,
        "cus_phone": userdata.cus_phone,
    }
    querydetail = Query.objects.filter(cus_email_q=x)
    return render(request,'deshbord.html',{'userdata':userdata,'querydetail':querydetail})



def edit(request,pk):
    editdata = Query.objects.get(id=pk)
    email = editdata.cus_email_q   # yaha query model se email nikal rahe hai
    userdata = Customer.objects.get(cus_email=email)
    return render(request,'deshbord.html',{'userdata':userdata , 'editdata':editdata})
    

def quaryupdate(request,pk):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        query = request.POST.get('query')
        print("..............")
        old_query = Query.objects.get(id=pk)
        print("..............",old_query)
        old_query.cus_name_q = name
        old_query.cus_email_q = email
        old_query.cus_query_q = query
        old_query.save()
        allquery = Query.objects.filter(cus_email_q=email)
        userdata = Customer.objects.get(cus_email=email)
        return render(request,'deshbord.html',{'userdata':userdata,'allquery':allquery})
    

def delete(request,pk):
    deletedata = Query.objects.get(id=pk)
    email = deletedata.cus_email_q
    deletedata.delete()
    allquery = Query.objects.filter(cus_email_q=email)
    userdata = Customer.objects.get(cus_email=email)
    return render(request,'deshbord.html',{'allquery':allquery,'userdata':userdata})


def search(request, pk):
    userdata = Customer.objects.get(id=pk)
    if request.method == "POST":
        searchData = request.POST.get('search')
        all_data = Query.objects.filter(
            Q(cus_name_q__icontains=searchData) |
            Q(cus_email_q__icontains=searchData) |
            Q(cus_query_q__icontains=searchData)
        )
        return render(request, 'deshbord.html', {'userdata': userdata, 'all_data': all_data,'searchData':searchData})
    return render(request, 'deshbord.html', {'userdata': userdata, 'querydetail': Query.objects.all()})


# deshbord me offer ke liye 
def offer(request, pk):
    userdata = Customer.objects.get(id=pk)
    return render(request, 'deshbord.html', {
        'userdata': userdata,
        'offer': True
    })
