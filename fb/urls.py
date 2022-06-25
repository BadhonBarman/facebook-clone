from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('profile', views.user_profile, name='user_profile')
]
