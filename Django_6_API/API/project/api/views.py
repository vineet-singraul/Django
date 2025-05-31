from django.shortcuts import render
from django.http import JsonResponse
from .models import Student

from .serializers import StudentSerializer
# Create your views here.

def student_list(request):
    stu=Student.objects.all()
    print(stu)
    print(type(stu))
    serializer=StudentSerializer(stu,many=True)
    print(serializer)
    print(serializer.data)
    return JsonResponse(serializer.data,safe=False)

def student_detail(request):
    pass