from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('mens/',views.mens,name='mens'),
    path('womens/',views.womens,name='womens'),
    path('kides/',views.kides,name='kides'),
    path('electranics/',views.electranics,name='electranics'),
    path('grousary/',views.grousary,name='grousary'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),

    path('home/<int:pk>/',views.home1,name='home1'),
    path('mens/<int:pk>/',views.mens1,name='mens1'),
    path('womens/<int:pk>/',views.womens1,name='womens1'),
    path('kides/<int:pk>/',views.kides1,name='kides1'),
    path('electranics/<int:pk>/',views.electranics1,name='electranics1'),
    path('grousary/<int:pk>/',views.grousary1,name='grousary1'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
