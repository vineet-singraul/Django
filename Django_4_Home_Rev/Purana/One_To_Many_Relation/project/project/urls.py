
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',views.student,name='student'),
    path('department/',views.department,name='department'),
]
