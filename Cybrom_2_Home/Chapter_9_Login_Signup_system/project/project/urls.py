from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contect/',views.contect,name='contect'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('signupdata/',views.signupdata,name='signupdata'),
    path('logindata/',views.logindata,name='logindata'),
]
