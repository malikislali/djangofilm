from django.contrib import admin
from django.urls import path
#  . aynı dizin demek
from . import views

#http://127.0.0.1:8000/

#http://127.0.0.1:8000/movies
#http://127.0.0.1:8000/movies/3

#http://127.0.0.1:8000/movies/walking_deads


urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', views.home),
    path('home',views.home),
    path('movies',views.movies)
]
