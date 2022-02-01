import json
from django.http import JsonResponse
import base64
from test_platform.settings import BASE_DIR

UPLOAD_PATH = BASE_DIR.joinpath('api_app').joinpath('upload')
FILE_TYPE = ['csv', 'txt', 'jpg', 'jpeg', 'gif']


class Number:
    num = 0


def ping(request):
    """
    测试api
    json -- str  json.dumps  dict转化为json字符串
    str -- dict json.loads
    """
    return JsonResponse({"code": 10200, "message": "Welcome to API testing"})


def add_one(request):
    Number.num += 1
    return JsonResponse({"code": 10200, "data": {"number": Number.num}, "message": "success"})


def get_user(request, uid):
    """
    GET参数方式1: /user/1
    """
    if uid == 1:
        data = {"age": 22, "id": 1, "name": "tom"}
        return JsonResponse({"code": 10200, "data": data, "message": "success"})
    return JsonResponse({"code": 10101, "message": "user id null"})


def get_user2(request):
    """
    GET参数方式2： /user?uid=1
    """
    uid = request.GET.get('uid', '')
    if uid == '' or uid != 1:
        return JsonResponse({"code": 10101, "message": "user id null"})
    elif uid == 1:
        data = {"age": 22, "id": 1, "name": "tom"}
        return JsonResponse({"code": 10200, "data": data, "message": "success"})


def user_login(request):
    """
    POST
    """
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)
    if username == '' or password == '':
        return JsonResponse({'code': 10103, 'message': 'username or password is null'})
    if username != 'admin' or password != 'admin123':
        return JsonResponse({'code': 10104, 'message': 'username or password error'})
    else:
        return JsonResponse({'code': 10200, 'message': 'login success'})


def add_user(request):
    """
    POST: raw --> 后端对应未bytes类型 b''
    后端拿数据 request.body
    """
    text_str = request.body.decode('utf-8')
    text_dict = json.loads(text_str)
    uid = text_dict.get('id')
    uname = text_dict.get('name')
    data = {
        'uid': uid,
        'uname': uname
    }
    return JsonResponse({'code': 10200, 'message': 'add success', 'data': data})


def header(request):
    """
    获取头部信息： request.headers
    """
    token = request.headers.get('token', '')
    if token == '':
        return JsonResponse({'code': 10102, 'message': 'token is null'})
    return JsonResponse({'code': 10200, 'message': 'successful'})


def auth(request):
    """
    basic Auth: 解码：base64
    """
    # print(request.headers.get('Authorization'))
    auth_str = request.headers.get('Authorization', '')
    if auth_str == '':
        return JsonResponse({'code': 10102, 'message': 'Authorization is null'})
    auth_ = auth_str.split()[1]
    auth_user = base64.b64decode(auth_).decode('utf-8')
    user = auth_user.split(':')[0]
    pwd = auth_user.split(':')[1]
    if user != 'admin' or pwd != 'admin123456':
        return JsonResponse({'code': 10104, 'message': 'auth fail!'})
    else:
        return JsonResponse({'code': 10200, 'message': 'auth success'})


def upload(request):
    """
    request.FILES 获取上传的文件对象
    """
    file = request.FILES.get('file')
    file_type = file.name.split('.')[-1]
    if file_type not in FILE_TYPE:
        return JsonResponse({'code': 10103, 'message': 'file type error'})
    if file.size > 1048576:
        return JsonResponse({'code': 10104, 'message': 'file size is greater than 10M'})
    with(open(UPLOAD_PATH.joinpath(file.name), 'wb')) as f:
        for chunk in file.chunks():
            f.write(chunk)
    return JsonResponse({'code': 10200, 'message': 'upload success'})
