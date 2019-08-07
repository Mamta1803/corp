from django.contrib import admin
from django.urls import path
from conapp import views

urlpatterns = [
    path('', views.index),
    path('submit/', views.index),
]
