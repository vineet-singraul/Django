from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from app import views
from django.conf import settings   # type: ignore
from django.conf.urls.static import static   # type: ignore
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('mens/',views.mens,name='mens'),
    path('womens/',views.womens,name='womens'),
    path('kides/',views.kides,name='kides'),
    path('electranic/',views.electranic,name='electranic'),
    path('grousary/',views.grousary,name='grousary'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('signupdata/',views.signupdata,name='signupdata'),
    path('logindata/',views.logindata,name='logindata'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




