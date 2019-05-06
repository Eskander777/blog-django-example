"""blogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""
    
    
from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    
    # Страница для новой темы
    path('new_post/', views.new_post, name='new_post'),
    
    # Страница редактирования темы
    path('edit_post/<blog_id>/', views.edit_post, name='edit_post'),
    
]
