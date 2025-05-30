from django.shortcuts import render
from django.http import JsonResponse
from .serializers import StudentSerializer
from .models import Student
# Create your views here.


def student_list(req):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu,many=True)
    return JsonResponse(serializer.data,safe=False)
