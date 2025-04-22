from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contect/',views.contect,name='contect'),
    path('login/',views.login,name='login'),
    path('ragister/',views.ragister,name='ragister'),
    path('ragisterdata',views.ragisterdata,name='ragisterdata'),
]
