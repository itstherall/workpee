from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.contrib import admin
from login import views
from django.conf import settings

app_name = 'acc'

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_request, name="login"),
    re_path('signup/', views.signup, name='signup'),
    re_path('perfil/(?P<id>\d+)', views.perfil, name='perfil'),
    re_path('produto/(?P<id>\d+)', views.produto, name='produto'),
    re_path('produto/add', views.add_produto, name='add_produto'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
