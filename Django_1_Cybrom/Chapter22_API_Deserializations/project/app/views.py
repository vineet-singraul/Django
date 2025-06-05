from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io

# Create your views here.

@csrf_exempt
def stu_list(request):
    if request.method == 'POST':
        json_data = request.body
        print("Thise Is Json Data : ",json_data)
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        print(python_data)
        serializer =StudentSerializer(data = python_data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
            # return JsonResponse(res)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    


@csrf_exempt
def student_detail(request,pk):
    # print(pk)
    # print(request.method)
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        new_python_data = JSONParser().parse(stream)
        old_data = Student.objects.get(id=pk)
        # serializer = StudentSerializer(old_data, data=python_data, partial = True)
        serializer = StudentSerializer(old_data, data=new_python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated !!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    elif request.method == 'PATCH':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=python_data, partial = True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Partially Updated...!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')  
 
    elif request.method == 'DELETE':
        stu = Student.objects.filter(id=pk)
        if stu:
            stu = Student.objects.get(id=pk)
            stu.delete()
            res = {'msg': 'Data Deleted!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        else:
            res = {'msg': 'Not Present in database!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')