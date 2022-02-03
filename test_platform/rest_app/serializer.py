from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'  # indicate all fields in the model
        fields = ['id', 'username', 'email', 'is_staff']
        # exclude = ['users']  # excluded from the serializer.
