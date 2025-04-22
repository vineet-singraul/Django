from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contect/',views.contect,name='contect'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('registerdata/',views.registerdata,name='registerdata'),
]
