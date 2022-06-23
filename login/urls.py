from django.urls import path, include, re_path
from django.contrib import admin
from login import views



urlpatterns = [
    path('index/', views.index, name='home'),
    re_path('signup/', views.signup, name='signup'),

]
