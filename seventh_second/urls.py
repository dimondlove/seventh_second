"""
URL configuration for seventh_second project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from seventh import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('get/', views.get_student),
    path('filter/', views.get_filter),
    path('exclude/', views.get_exclude),
    path('twostudents/', views.get_two_students),
    path('save/', views.save),
    path('update/', views.update_student),
    path('delete/', views.delete_student),
    path('getspec/', views.get_spec),
    path('sort/', views.sort),
    path('getexact/', views.get_exact),
]
