from django.shortcuts import render
from .models import Student

def home(request):
    return render(request, "home.html", {'show_form': True})

def inserQuery(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        city = request.POST.get('city')
        about = request.POST.get('about')
        number = request.POST.get('number')

        Student.objects.create(
            name=name,
            email=email,
            image=image,
            city=city,
            about=about,
            number=number
        )

        return render(request, "home.html", {
            "msg": "Data inserted successfully!",
            "show_form": True
        })

    return render(request, "home.html", {'show_form': True})


def allquery(request):
    data = Student.objects.all()
    return render(request, "home.html", {'userdata': data})


def edit(request,pk):
   editUserdata = Student.objects.get(id=pk)
   return render(request,'home.html',{'editUserdata':editUserdata})



def editedData(request,pk):
    email=request.POST.get('email')
    city=request.POST.get('city')
    about=request.POST.get('about')
    number=request.POST.get('number')
    image=request.FILES.get('image')
    oldData=Student.objects.get(id=pk)
    oldData.city=city
    oldData.about=about
    oldData.number=number
    oldData.image=image
    oldData.save()
    data = Student.objects.all()
    return render(request,'home.html',{'userdata': data})



def delete(request,pk):
    user = Student.objects.get(id=pk)
    user.delete()
    data = Student.objects.all()
    return render(request,'home.html',{'userdata': data})