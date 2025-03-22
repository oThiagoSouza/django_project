from django.urls import path
from . import views

urlpatterns = [
    path('home', views.ver_home, name='ver_home'),
    path('home2', views.ver_home2, name='ver_home2')
]