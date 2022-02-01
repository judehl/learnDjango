# -*- coding: utf-8 -*-
# @Time    : 2022/1/31 21:41
# @Author  : hk
from django.urls import path
from api_app import views

urlpatterns = [
    path('v1/add_one', views.add_one),
    path('v1/user/<int:uid>/', views.get_user),
    path('v1/user2/', views.get_user2),
    path('v1/login/', views.user_login),
    path('v1/add_user/', views.add_user),
    path('v1/header/', views.header),
    path('v1/auth/', views.auth),
    path('v1/upload/', views.upload),
]
