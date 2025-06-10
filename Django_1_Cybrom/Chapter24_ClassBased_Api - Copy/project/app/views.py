from app.models import Student
from app.serializers import StudentSerializer
# from rest_framework import mixins
# from rest_framework import generics

from rest_framework import generics


# class Stulist(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#             queryset = Student.objects.all()
#             serializer_class = StudentSerializer

#             def get(self, request, *args, **kwargs):
#                 return self.list(request, *args, **kwargs)

#             def post(self, request, *args, **kwargs):
#                 return self.create(request, *args, **kwargs)
    



# class Studetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#             queryset = Student.objects.all()
#             serializer_class = StudentSerializer

#             def get(self, request, *args, **kwargs):
#                 return self.retrieve(request, *args, **kwargs)

#             def put(self, request, *args, **kwargs):
#                 return self.update(request, *args, **kwargs)

#             def delete(self, request, *args, **kwargs):
#                 return self.destroy(request, *args, **kwargs)






# ++++++++++++++++++++++ Using generic class-based views +++++++++++
class Stulist(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class Studetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer