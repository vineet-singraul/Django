from rest_framework import viewsets
from .models import Student
from app.serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer