
from django.urls import path

from . import views

app_name = 'footage'
urlpatterns = [
    path('<int:uuid>/', views.detail, name='detail'),
    path('upload/', views.upload, name='upload'),
]
