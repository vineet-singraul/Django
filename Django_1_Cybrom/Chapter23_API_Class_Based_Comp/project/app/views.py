from django.shortcuts import render
from app.models import Student
from app.serializers import StudentSerializer
from rest_framework.views import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET','POST'])
def movie_list(request):
    if request.method == 'GET':
        snippets = Student.objects.all()
        serializer = StudentSerializer(snippets, many=True)
        return Response(serializer.data)
   

    elif  request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET','PUT','DELETE','PATCH'])
def stu_detail(request,pk):
    id = Student.objects.filter(id=pk)
    if id:
        if request.method == 'GET':
                snippet = Student.objects.get(id=pk)
                serializer = StudentSerializer(snippet)
                return Response(serializer.data)

        elif request.method == 'PUT':
                snippet = Student.objects.get(id=pk)
                serializer = StudentSerializer(snippet, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
        
        elif request.method == 'PATCH':
                snippet = Student.objects.get(id=pk)
                serializer = StudentSerializer(snippet, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)

        elif request.method == 'DELETE':
                snippet = Student.objects.get(id=pk)
                snippet.delete()
                return Response({"msg": "Deteted"})