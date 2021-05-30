from django.shortcuts import render
from django.views.decorators.http import require_GET


# 退出登录
@require_GET
def logout(request):
    request.session.clear()
    return render(request, 'login.html',context={'tips': '','header': '小区管理员'})


# 首页登录view
@require_GET
def index(request):
    context = {'tips': '', 'header': '欢迎使用 小区进出管理系统'}
    return render(request, 'login.html', context=context)


# 登录验证，并跳转至管理员页面
@require_GET
def manage(request):
    context = {}
    return render(request, 'manage.html', context=context)


# 背景页面
@require_GET
def blackboard(request):
    context = {}
    return render(request, 'blackboard.html', context=context)


# 数据统计分析model-view
@require_GET
def cms_statistics(request):
    context = {}
    return render(request, 'common')











