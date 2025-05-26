from django.shortcuts import render
from .models import Student
# Create your views here.



def home(request):
    return render(request,'home.html')



def inserdata(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        gender = request.POST.get('gender')
        number = request.POST.get('number')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        Student.objects.create(name=name, city=city, gender=gender, number=number, email=email, image=image)
        msg = "Data Inserted Successfully!"
        return render(request, 'home.html', {'msg': msg, 'Show': True}) 

    return render(request, 'home.html', {'Show': True}) 

def showtable(request):
    data = Student.objects.all()
    return render(request, 'home.html', {'data': data})



def editopen(request,pk):
    forEdit = Student.objects.get(id=pk)
    return render(request,'home.html',{'forEdit':forEdit})



def updateEdited(request, pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        number = request.POST.get('number')
        email = request.POST.get('email')
        image = request.FILES.get('image')

        old_Data = Student.objects.get(id=pk)
        old_Data.name = name
        old_Data.city = city
        old_Data.number = number
        old_Data.email = email

        if image:
            old_Data.image = image

        old_Data.save()

        data = Student.objects.all()
        msg = "Data updated successfully!"
        return render(request, 'home.html', {'data': data, 'msg': msg})


def delete(request,pk):
    data1 = Student.objects.get(id=pk)
    data1.delete()
    data = Student.objects.all()
    msg = "Data Deleted successfully!"
    return render(request, 'home.html', {'data': data, 'msg': msg})
