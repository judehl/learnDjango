from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_app.serializer import UserSerializer
from rest_app.common import response, Error

"""
# fvb -> function based view 

from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_view(request):
    if request.method == 'GET':
        return JsonResponse({'msg': "查询"})
    elif request.method == 'POST':
        return JsonResponse({'msg': "添加"})
    elif request.method == 'PUT':
        return JsonResponse({'msg': "修改"})
    elif request.method == 'DELETE':
        return JsonResponse({'msg': "删除"})
"""


# Create your views here.
def hello(request):
    return JsonResponse({'success': True})


# cvb -> class based view
class UserView(APIView):

    def get(self, request, *args, **kwargs):
        """
        查询
        request.query_params : get请求 params参数
        kwargs.get('uid') ： get 请求 url取参数 /api/<int:uid>/
        """
        # users = User.objects.all()
        # user_list = []
        # 1、方式1
        # for user in users:
        # user_dict = {
        #     "url": "http://127.0.0.1:8080/rest/v1/user/{uid}/".format(uid=user.id),
        #     "username": user.username,
        #     "email": user.email,
        #     'is_staff': user.is_staff
        # }
        # user_list.append(user_dict)

        # 2、方式2 model_to_dict
        # for user in users:
        # user_list.append(model_to_dict(user))

        # 3、序列化 serializers
        # ser = UserSerializer(users, many=True)  # many指定拿的数据复数多个,默认True
        # return response(data=ser.data)
        uid = kwargs.get('uid')
        if uid is not None:
            try:
                user = User.objects.get(pk=uid)
            except User.DoesNotExist:
                return response(error=Error.USER_ID_NULL)
            ser = UserSerializer(instance=user, many=False)
            return response(data=ser.data)
        else:
            user = User.objects.all()
            ser = UserSerializer(instance=user, many=True)
            return response(data=ser.data)

    def post(self, request, *args, **kwargs):
        """
        添加
        request.data : post请求取参数
        """
        return JsonResponse({'msg': "添加"})

    def put(self, request, *args, **kwargs):
        """
        修改
        """
        return JsonResponse({'msg': "修改"})

    def delete(self, request, *args, **kwargs):
        """
        删除
        """
        return JsonResponse({'msg': "删除"})
