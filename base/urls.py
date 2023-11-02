from django.urls import path
from base import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('home2/', views.home2, name='home2'),
]
