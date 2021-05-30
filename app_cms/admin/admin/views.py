import json
from app_cms import models
from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.http import require_GET, require_POST


# 小区管理员信息管理model-view
@require_GET
def admin(request):
    context = {'header': '小区管理员'}
    return render(request, 'common/admin/admin.html', context)


# 小区管理员信息管理model-view
@require_GET
def admin_add(request):
    return render(request, 'common/admin/admin_add.html')


@require_GET
def admin_edit(request):
    path = request.get_full_path()
    admin_id = path.split('/')[-1]
    context = {'item': {}}
    if admin_id:
        single_admin = models.Admin.objects.get(id=admin_id)
        context['item'] = model_to_dict(single_admin)
    return render(request, 'common/admin/admin_edit.html', context=context)


# 小区管理员列表数据获取
@require_POST
def admin_list(request):
    admin_lists = models.Admin.objects.all()
    data = []
    for i in admin_lists:
        data.append(model_to_dict(i))
    return JsonResponse(data, safe=False)


@require_POST
def admin_save(request):
    name = request.POST['name']
    password = request.POST['password']
    admin_id = request.POST['id']
    if admin_id == '':
        admin_id = None
    else:
        admin_id = int(admin_id)
    single_admin = models.Admin(id=admin_id, name=name, password=password)
    single_admin.save()
    result = {'message': '添加成功', 'code': 200}
    return JsonResponse(result)


@require_POST
def admin_update(request):
    name = request.POST['name']
    password = request.POST['password']
    admin_id = request.POST['id']
    rows = models.Admin.objects.filter(id=admin_id).update(name=name, password=password)
    result = {}
    if rows:
        result = {'message': '更新成功', 'code': 200}
    return JsonResponse(result)


@require_POST
def admin_delete(request):
    admin_id = request.POST['cmsAdminId']
    single_admin = models.Admin.objects.filter(id=admin_id)
    result = {'code': 200, 'message': ''}
    if single_admin.delete()[0]:
        result = {'message': '删除成功', 'code': 200}
    return JsonResponse(result)


# 验证账号
@require_POST
def valid_account(request):
    name = request.POST.get('username')
    password = request.POST.get('password')
    single_model = models.Admin.objects.get(name=name, password=password)
    if single_model.id:
        result = {'message': '登录成功', 'statusCode': 200}
        request.session['admin'] = single_model.serialize()
    else:
        result = {'message': '账号或密码错误', 'statusCode': 201}
    return JsonResponse(result)


@require_GET
def statistic(request):
    return render(request, "common/statistic/statistic.html", context={})


# 数据分析获取接口
@require_POST
def statistic_api(request):
    func_type = request.POST['type']
    # 格式yyyy-mm
    time = request.POST['time']
    t2l = time.split('-')
    result = {'data': [], 'type': func_type, 'time': time}
    if func_type == 'temperature':
        result['message'] = '进出人员体温分析'
        # 36.2-37.1
        temperatures = models.CheckLog.objects.filter(sign_time__year=t2l[0], sign_time__month=t2l[1]).\
            order_by('temperature').values('temperature')
        result['total'] = len(temperatures)
        t_1, t_2, t_3 = 0, 0, 0
        for i in temperatures:
            i = i['temperature']
            if i <= 36.2:
                t_1 += 1
            elif 36.2 < i < 37.1:
                t_2 += 1
            else:
                t_3 += 1
        # 进出人员的体温信息
        d = [{'name': '正常(36.2~37.1)', 'value': t_2}, {'name': '发烧(37.1及以上)', 'value': t_3},
             {'name': '低烧(36.2及以下)', 'value': t_1}]
        result['data'] = d
    elif func_type == 'matter':
        # 临时人员来访事宜统计
        result['message'] = '临时人员来事宜分析'
        t = time.split('-')
        c = models.CheckLog.objects.filter(sign_time__year=t[0], sign_time__month=t[1]).\
            values('matter').distinct()
        # 数据处理
        total = 0
        for i in c:
            values = models.CheckLog.objects.filter(matter=i['matter'])
            num = len(values)
            result['data'].append({'name': i['matter'], 'value': num})
            total += num
        result['total'] = total
    elif func_type == 'job':
        result['message'] = '临时人员职业统计'
        c = models.CheckLog.objects.filter(sign_time__year=t2l[0], sign_time__month=t2l[1]).\
            values('user_type').distinct()
        total = 0
        for i in c:
            values = models.CheckLog.objects.filter(user_type=i['user_type'])
            num = len(values)
            result['data'].append({'name': i['user_type'], 'value': num})
            total += num
        result['total'] = total
    else:
        result['message'] = '意料之外的情况发生了'
    return JsonResponse(result, safe=False)
