from django.urls import path
from app.views import home,register,login,logout

urlpatterns = [
    path("",home,name='home'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout')
]
