from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse,JsonResponse
from . import views
urlpatterns=[
path('',views.login,name="login"),
path('register',views.register,name="register"),
path('home',views.home,name="home"),
path('logout',views.logout,name="logout"),
path('post',views.post,name="post"),
]