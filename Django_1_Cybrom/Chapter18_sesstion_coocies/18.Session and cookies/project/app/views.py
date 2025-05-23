from django.shortcuts import render

# Create your views here.
def home(req):
    # print("Hello......")
    # print(request.COOKIES)
    # print(type(request.COOKIES))
    return render(req,'app/register.html')

def register(req):
    if req.method=='POST':
        print("Hell...........")
        uname = req.POST.get('user id')
        passw = req.POST.get('p1')
        dob = req.POST.get('Brithday')
        email = req.POST.get('email')
        phone = req.POST.get('num')
        x = render(req,'app/login.html')
        x.set_cookie("name",uname)
        x.set_cookie('passw',passw)
        x.set_cookie('dob',dob)
        x.set_cookie('email',email)
        x.set_cookie('phone',phone)
        return x

def login(req):
    if req.method=='POST':
        x = req.POST.get('email')
        p=req.POST.get('password')
        n=req.COOKIES['name']
        pa=req.COOKIES['passw']
        do=req.COOKIES['dob']
        e=req.COOKIES['email']
        ph=req.COOKIES['phone']
        userdata={'name':n,'dob':do,'email':e,'phone':ph}
        print(ph,n,do,e,pa)
        print(x,p)
        if (x==e and p==pa):
            return render(req,'app/dashboard.html',{'userdata':userdata})
        else:
            return render(req,'app/login.html')

    else:
        return render(req,'app/login.html')

def logout(request):
    resp = render(request,'app/register.html')
    resp.delete_cookie('name')
    resp.delete_cookie('passw')
    resp.delete_cookie('dob')
    resp.delete_cookie('email')
    resp.delete_cookie('phone')
    return resp



