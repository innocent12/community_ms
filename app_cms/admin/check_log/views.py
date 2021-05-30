from app_cms import models
from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.http import require_GET, require_POST


# 人员进出登记model-view
@require_GET
def check(request):
    context = {'header': '小区人脸识别登记'}
    return render(request, 'common/checklog/check.html', context=context)


@require_POST
def list(request):
    check_list = models.CheckLog.objects.all()
    data = []
    for i in check_list:
        data.append(model_to_dict(i))
    return JsonResponse(data, safe=False)


@require_GET
def add(request):
    context = {}
    return render(request, 'common/checklog/check_add.html', context=context)


@require_GET
def add_with_img(request):
    image = request.POST.get('image')
    context = {'image': image}
    print(image)
    return render(request, 'common/checklog/check_add.html', context=context)


@require_POST
def save(request):
    c = models.CheckLog()
    c.name = request.POST['name']
    c.user_type = request.POST['user_type']
    c.temperature = request.POST['temperature']
    c.matter = request.POST['matter']
    c.comment = request.POST['comment']
    user_id = request.POST['user_id']
    if user_id != '':
        c.user_id = user_id
    c.user_type = request.POST['user_type']
    c.save()
    data = {'message': '添加成功'}
    return JsonResponse(data)


@require_POST
def delete(request):
    check_id = request.POST['cmsCheckLogId']
    single_check = models.CheckLog.objects.filter(id=check_id)
    result = {'message': '', 'code': 200}
    if single_check:
        result['message'] = '删除成功'
    return JsonResponse(result)


@require_POST
def update(request):
    log = models.CheckLog()
    log.id = request.POST.get('id')
    log.name = request.POST['name']
    log.user_id = request.POST['user_id']
    log.user_type = request.POST['user_type']
    log.temperature = request.POST['temperature']
    log.matter = request.POST['matter']
    log.comment = request.POST['comment']
    log.save()
    data = {'message': '保存成功', 'code': 200}
    return JsonResponse(data)


@require_GET
def edit(request):
    path = request.get_full_path().split('/')
    check_id = path[-1]
    context = {}
    if check_id:
        single_check = models.CheckLog.objects.get(id=check_id)
        context['item'] = model_to_dict(single_check)
    return render(request, 'common/checklog/check_edit.html', context=context)
