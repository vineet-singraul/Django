"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('inserQuery/',views.inserQuery,name='inserQuery'),
    path('allquery/',views.allquery,name='allquery'),
    # edit btn per click karne per
    path('edit<int:pk>/',views.edit,name='edit'),
    # Edite karne ke liye 
    path('editedData<int:pk>/',views.editedData,name='editedData'),
    #delete ke liye hai 
    path('delete<int:pk>/',views.delete,name='delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
