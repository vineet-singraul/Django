from django.contrib import admin
from .models import Student

# admin.site.register(Student)

@admin.register(Student)    # Table create ker dega admin panel me
class StudentAdmin(admin.ModelAdmin):
    list_display=["id","stu_name","stu_email","stu_contect","stu_city"]