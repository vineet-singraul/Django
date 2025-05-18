from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contect/',views.contect,name='contect'),
    path('new/',views.new,name='new'),
]
                                                                                                                                                                                                      