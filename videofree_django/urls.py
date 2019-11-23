
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('footage/', include('footage.urls')),
    path('user/', include('user.urls')),

    path('admin/', admin.site.urls),
]
