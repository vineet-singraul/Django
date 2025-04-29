from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('mens/', views.mens, name='mens'),
    path('womens/', views.womens, name='womens'),
    path('kides/', views.kides, name='kides'),
    path('electranics/', views.electranics, name='electranics'),
    path('grousary/', views.grousary, name='grousary'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('signupdata/', views.signupdata, name='signupdata'),
    path('logindata/', views.logindata, name='logindata'),
    path('logout/', views.logout, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)