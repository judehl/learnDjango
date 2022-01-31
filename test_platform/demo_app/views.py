# kill -9 `lsof -i tcp:8000 | awk '{print $2}'| tail -n 1`

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.

def hello(request):
    print(request.body)
    print(request.path)
    print(request.method)
    if request.method == 'GET':
        return render(request, 'demo_app/hello.html')  # demo_app对应templates中目录
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        if username == 'admin' and pwd == 'admin123':
            # return render(request, 'demo_app/hello.html', {"msg": '登陆成功'})
            return JsonResponse({"success": True, "message": "登陆成功"})
        else:
            # return render(request, 'demo_app/hello.html', {"msg": '登陆失败'})
            return JsonResponse({"success": False, "message": "登陆失败"})


def calculator(request):
    """
    计算器
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'demo_app/calculator.html')  # demo_app对应templates中目录
    if request.method == 'POST':
        num_a = request.POST.get('number_a')
        num_b = request.POST.get('number_b')
        c = int(num_a) + int(num_b)
        return render(request, "demo_app/calculator.html", {'result': c})