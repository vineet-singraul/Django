from django.contrib import admin
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("student_detail/<int:pk>/",student_detail,name='name'),
    path("stu_list/",stu_list,name='stu_list')
]