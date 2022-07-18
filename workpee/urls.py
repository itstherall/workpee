from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'root'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

urlpatterns += staticfiles_urlpatterns()
