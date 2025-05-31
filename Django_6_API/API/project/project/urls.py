from django.contrib import admin
from django.urls import path
from api import views
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu_list/',student_list),
    path('stu_info/<int:pk>',student_detail),

]
