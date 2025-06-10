from django.urls import path
from app import views
urlpatterns = [
   path('list/',views.movie_list,name="movie_list"),
   path('list/<int:pk>/',views.movie_detail,name="movie_detail"),
   path('stream/',views.stream_list,name='stream_list'),
   path('stream/<int:pk>/',views.stream_detail,name='stream_detail'),
]