
from django.urls import path

from . import views

app_name = 'footage'
urlpatterns = [
    path('', views.detail, name='detail'),
]
