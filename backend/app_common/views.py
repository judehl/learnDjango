from django.contrib import auth
from rest_framework.authtoken.models import Token
from app_common.utils.base_view import BaseAPIView
from


class TestView(BaseAPIView):
    authentication_classes = []

    def get(self, request):
        return self.response()


class LoginView(BaseAPIView):
    """
    登录接口
    """
    authentication_classes = []

    def post(self, request):
        """
        登录账号，获取token
        """
        login_username = request.POST.get('username', '')
        login_password = request.POST.get('password', '')
        if login_username == '' or login_password == '':
            return self.response(error=self.USER_OR_PAWD_NULL)
        else:
            user = auth.authenticate(usrname=login_password, pwd=login_password)
            if user is not None and user.is_active:
                auth.login(request, user)  # 登录获取token
                token = Token.objects.filter(user=user)
                token.delete()
                token = Token.objects.create(user=user)
                return self.response(data={'token': str(token)})
            else:
                return self.response(error=self.USER_OR_PAWD_ERROR)

    def delete(self, request):
        """
        登出并删除token
        """
        userId = request.POST.get('user')
        token = Token.objects.filter(user=userId)
        token.delete()
        return self.response()
