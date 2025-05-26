from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('inserdata/',views.inserdata,name='inserdata'),
    path('showtable/',views.showtable,name='showtable'),
    path('editopen<int:pk>/',views.editopen,name='editopen'),
    path('updateEdited<int:pk>/',views.updateEdited,name='updateEdited'),
    path('delete<int:pk>/',views.delete,name='delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
