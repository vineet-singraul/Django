from django.shortcuts import render
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
    # return render(request , "ragisterdata.html")
    # print("==================",request.method)
    # print(request.POST)
    username = request.POST.get('username')
    email = request.POST.get('email')
    detail = request.POST.get('detail')
    phone = request.POST.get('phone')
    dob = request.POST.get('dob')
    subscribe = request.POST.get('subscribe')
    gender = request.POST.get('gender')
    image = request.POST.get('profile-pic')
    resume = request.POST.get('resume')
    password = request.POST.get('password')

    user = Student.objects.filter(stu_email = email)

    if user:
        msg = "user Alrady Exits"
        return render(request , 'ragister.html' , {"msg":msg})

    else:
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

 
