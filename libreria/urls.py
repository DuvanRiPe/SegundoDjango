from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index),
    path('crear', views.crear, name=''),
    path('editar', views.crear, name=''),
    
]
