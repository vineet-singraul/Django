from django.contrib import admin
from django.urls import path,include
from app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]
