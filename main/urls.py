"""algorithm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('luhnaDate/', views.luhnaDate, name='luhnaDate'),
    path('luhna/<str:wynik>/', views.luhna, name='luhna'),
    path('cezarDate/', views.cezarDate, name='cezarDate'),
    path('cezar/<str:wynik>/', views.cezar, name='cezar'),
    path('binarnyDate/', views.binarnyDate, name='binarnyDate'),
    path('binarny/<str:wynik>/', views.binarny, name='binarny'),
    path('resztaDate/', views.resztaDate, name='resztaDate'),
    path('reszta/<str:wynikLista0>/<str:wynikLista1>/<str:wynikLista2>/<str:wynikLista3>/<str:wynikLista4>/<str:wynikLista5>/', views.reszta, name='reszta'),
    
    path('francjaDate/', views.francjaDate, name='francjaDate'),
    path('francja/<str:wynik>/', views.francja, name='francja'),
    path('polskaDate/', views.polskaDate, name='polskaDate'),
    path('polska/<str:wynik>/', views.polska, name='polska'),
    path('euklidesDate/', views.euklidesDate, name='euklidesDate'),
    path('euklides/<str:wynik>/', views.euklides, name='euklides'),
    path('wyborDate/', views.wyborDate, name='wyborDate'),
    path('wybor/<str:wynik>/', views.wybor, name='wybor'),
    path('babelkoweDate/', views.babelkoweDate, name='babelkoweDate'),
    path('babelkowe/<str:wynik>/', views.babelkowe, name='babelkowe'),
]
