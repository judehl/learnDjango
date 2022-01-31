# -*- coding: utf-8 -*-
# @Time    : 2022/1/29 11:11
# @Author  : hk

from django.http import JsonResponse
from django.shortcuts import render


def add(request):
    """
    计算加法
    :param request:
    :return:
    """
    if request.method == 'POST':
        a = request.POST.get('number_a0', "")
        b = request.POST.get('number_b0', "")
        if a == '' or b == '':
            return JsonResponse({'success': False, "message": '参数错误'})
        sum = int(a) + int(b)
        return JsonResponse(
            {'success': True, 'message': '成功', "data": {'sum': sum}})
    return JsonResponse({'success': False, 'message': '请求方法错误'})


def sub(request):
    """
    计算减法
    :param request:
    :return:
    """
    if request.method == 'POST':
        a = request.POST.get('number_a1', "")
        b = request.POST.get('number_b1', "")
        if a == '' or b == '':
            return JsonResponse({'success': False, "message": '参数错误'})
        sub = int(a) - int(b)
        return JsonResponse(
            {'success': True, 'message': '成功', "data": {'sub': sub}})
    return JsonResponse({'success': False, 'message': '请求方法错误'})


def mul(request):
    """
    计算乘法
    :param request:
    :return:
    """
    if request.method == 'POST':
        a = request.POST.get('number_a2', "")
        b = request.POST.get('number_b2', "")
        if a == '' or b == '':
            return JsonResponse({'success': False, "message": '参数错误'})
        mul = int(a) * int(b)
        return JsonResponse(
            {'success': True, 'message': '成功', "data": {'mul': mul}})
    return JsonResponse({'success': False, 'message': '请求方法错误'})


def div(request):
    """
    计算除法
    :param request:
    :return:
    """
    if request.method == 'POST':
        a = request.POST.get('number_a3', "")
        b = request.POST.get('number_b3', "")
        if a == '' or b == '':
            return JsonResponse({'success': False, "message": '参数错误'})
        div = int(a) / int(b)
        return JsonResponse(
            {'success': True, 'message': '成功', "data": {'div': div}})
    return JsonResponse({'success': False, 'message': '请求方法错误'})
