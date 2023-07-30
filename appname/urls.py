from django.contrib import admin
from django.urls import path
from appname import views

urlpatterns = [
    path("", views.index, name='home'),
    path("aout", views.aout, name='aout'),
    path("services", views.services, name='services'),
    path("cotact", views.cotact, name='cotact'),
]
