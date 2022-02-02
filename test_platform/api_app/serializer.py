# -*- coding: utf-8 -*-
# @Time    : 2022/2/2 16:00
# @Author  : hk

from django.contrib.auth.models import User
from rest_framework import serializers


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
