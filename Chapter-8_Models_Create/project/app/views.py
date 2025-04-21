from django.shortcuts import render # type: ignore
from .models import Student
# Create your views here.


def home(request):
    data = {'name':'vineet'}
    return render(request, "comman.html" , {"data":data})

def about(request):
    return render(request , "about.html")

def contect(request):
    return render(request , "contect.html")

def ragister(request):
    return render(request , "ragister.html")

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print("++++++++++++++++++++++",email)
        print("++++++++++++++++++++++",password)
    else :
        return render(request , "login.html")

def ragisterdata(request):
    # print("==================",request.method)
    # print(request.POST)
    username = request.POST.get('username')
    email = request.POST.get('email')
    detail = request.POST.get('detail')
    phone = request.POST.get('phone')
    dob = request.POST.get('dob')
    subscribe = request.POST.get('subscribe')
    gender = request.POST.get('gender')
    image = request.FILES.get('profile-pic')
    resume = request.FILES.get('resume')
    password = request.POST.get('password')
    cpassword = request.POST.get('cpassword')

    user = Student.objects.filter(stu_email = email)
    if user:
        msg = "user Alrady Exits"
        return render(request , 'ragister.html' , {"msg":msg})

    else:
        if password == cpassword:
                Student.objects.create( stu_name = username,
                            stu_email = email,
                            stu_detail = detail,
                            stu_phone = phone,
                            stu_dob = dob,
                            stu_quali = subscribe,
                            stu_gender = gender,
                            stu_image = image,
                            stu_resume = resume,
                            stu_pass = password  
                         )
                msg = "Ragistration Succesfull"
                return render(request , "login.html" , {"msg":msg})
        else:
            msg = "Password and Cpassword is Not match : "
            userdata = {
                'username':username,
                'email':email,
                'detail':detail,
                'phone':phone,
                'dob':dob,
                'subscribe':subscribe,
                'gender':gender,
                'image':image,
                'resume':resume}
            return render(request,'ragister.html',{'msg':msg,'data':userdata})

 
def logindata(request):
    if request.method == 'POST':
        e = request.POST.get('email')
        p = request.POST.get('password')

        user = Student.objects.filter(stu_email = e)
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ : ",user)
        if user:
            userdata = Student.objects.get(stu_email = e)
            print("User Data : ",userdata.stu_name)
            print("User Data : ",userdata.stu_email)
            p1 = userdata.stu_pass
             
            if p == p1:
                print(p,p1)
                u = request.POST.get('username')
                return render(request,'dashbord.html',{'userdata':userdata})         
            
            else:
                pmsg = 'password Not Match :'
                return render(request,'login.html',{'email':e,'pmsg':pmsg})

        else: 
            msg = 'email not exits :'
            return render(request,'ragister.html',{'msg':msg})
        
    else:
        return render(request,'login.html')
