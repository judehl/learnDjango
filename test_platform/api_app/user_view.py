# -*- coding: utf-8 -*-
# @Time    : 2022/2/2 16:04
# @Author  : hk
from django.contrib.auth.models import User
from rest_framework import viewsets
from api_app.serializer import UserSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
