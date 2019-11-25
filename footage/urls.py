
from django.urls import path

from . import views

app_name = 'footage'
urlpatterns = [
    path('', views.detail, name='detail'),
    path('upload/', views.upload, name='upload'),
]
