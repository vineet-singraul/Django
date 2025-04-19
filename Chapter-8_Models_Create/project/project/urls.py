from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contect/',views.contect,name='contect'),
    path('ragister/',views.ragister,name='ragister'),
    path('login/',views.login,name='login'),
    path('ragisterdata/',views.ragisterdata,name='ragisterdata'),
    path('logindata/',views.logindata,name='logindata')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
