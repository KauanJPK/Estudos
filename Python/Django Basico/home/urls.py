from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.show_homepages, name='show_homepages'),
    path('show/cadastro/', views.show_cadastro, name='show_cadastro'),
]
