from django.contrib import admin
from django.urls import path,include
from app.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]