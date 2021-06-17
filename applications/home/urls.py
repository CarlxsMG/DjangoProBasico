from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('home', views.HomeView.as_view()),
    path('home-list', views.HomeListView.as_view())
]
