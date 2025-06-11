from rest_framework import viewsets
from .models import Student
from app.serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated

class StudentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    permission_classes = [IsAuthenticated]

    queryset = Student.objects.all()
    serializer_class = StudentSerializer