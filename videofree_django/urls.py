
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('footage/', include('footage.urls')),
    path('user/', include('user.urls')),

    path('admin/', admin.site.urls),
]

if settings.DEBUG is True:
    urlpatterns += static('/media/', document_root='/home/joe/projects/videofree_django/media')