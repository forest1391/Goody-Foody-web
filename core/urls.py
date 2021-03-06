"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index),
    path('analyze/', views.analyze),
    path('coming/', views.coming),
    path('contact/', views.contact),
    path('single/', views.single),
    path('community/', views.community),
    path('login/', views.login),
    path('communitypage/', views.communitypage),
    path('communitypage2/', views.communitypage2),
    path('Userintroduction/', views.Userintroduction),
    path('consult/', views.consult),
    path('menu/', views.menu),
    path('information/', views.information),
    path('comment/', views.comment),
    path('consultchatroom/', views.consultchatroom),
    path('menuadd/', views.menuadd),
    path('Storeinformation/', views.Storeinformation),
    path('map/', views.map)
]
