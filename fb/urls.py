from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index_page, name='index'),
    # path('signup', views.signup, name='signup'),
    path('profile', views.user_profile, name='profile'),
    path('home', views.home, name='home')
]
