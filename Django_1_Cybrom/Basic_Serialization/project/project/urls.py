from django.contrib import admin
from django.urls import path
from .views import student_detail, student_list

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("stu_info/<int:pk>/", student_detail, name="student_detail"),
    path("stu_list/", student_list, name="student_list"),
]
