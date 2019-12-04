
from django.urls import path

from . import views

app_name = 'footage'
urlpatterns = [
    path('<str:key>/', views.detail, name='detail'),
    path('upload/', views.upload, name='upload'),
]
