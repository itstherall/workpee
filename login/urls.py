from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.contrib import admin
from login import views
from django.conf import settings

app_name = 'login'

urlpatterns = [
    path('', views.index, name='home'),
    re_path('signup/', views.signup, name='signup'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
