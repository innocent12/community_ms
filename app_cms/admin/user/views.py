from app_cms import models
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.forms.models import model_to_dict
from django.views.decorators.http import require_GET, require_POST


class ResidentView(View):

    # 小区居民model-view
    @staticmethod
    @require_GET
    def resident(request):
        context = {'header': '小区业主管理'}
        return render(request, 'common/resident/resident.html', context=context)

    @staticmethod
    @require_POST
    def list(request):
        resident_list = models.Residents.objects.all()
        data = []
        for i in resident_list:
            data.append(model_to_dict(i))
        return JsonResponse(data, safe=False)

    @staticmethod
    @require_GET
    def add(request):
        context = {}
        return render(request, 'common/resident/resident_add.html', context=context)

    @staticmethod
    @require_POST
    def save(request):
        resident = models.Residents()
        s_id = request.POST['id']
        if s_id != '':
            resident.id = int(s_id)
        resident.name = request.POST['name']
        resident.age = request.POST['age']
        resident.sex = request.POST['sex']
        resident.phone = request.POST['phone']
        resident.address = request.POST['address']
        resident.job = request.POST['job']
        resident.bce_user_id = request.POST['bce_user_id']
        resident.save()
        data = {'message': '添加成功', 'user_id': resident.id, 'type': resident.job, 'name': resident.name}
        return JsonResponse(data)

    @staticmethod
    @require_POST
    def delete(request):
        resident_id = request.POST['cmsResidentId']
        single_resident = models.Residents.objects.filter(id=resident_id)
        result = {'message': '', 'code': 200}
        if single_resident.delete()[0]:
            result = {'message': '删除成功', 'code': 200}
        return JsonResponse(result)

    @staticmethod
    @require_POST
    def update(request):
        resident = models.Residents()
        resident.id = request.POST['id']
        resident.name = request.POST['name']
        resident.age = request.POST['age']
        resident.sex = request.POST['sex']
        resident.phone = request.POST['phone']
        resident.address = request.POST['address']
        resident.job = request.POST['job']
        resident.bce_user_id = request.POST['bce_user_id']
        resident.save()
        data = {'message':'保存成功','code':200}
        return JsonResponse(data)

    @staticmethod
    @require_GET
    def edit(request):
        path = request.get_full_path()
        resident_id = path.split('/')[-1]
        context = {}
        if resident_id:
            single_resident = models.Residents.objects.get(id=resident_id)
            context['item'] = model_to_dict(single_resident)
        return render(request, 'common/resident/resident_edit.html', context=context)


class MigrantView(View):

    # 小区外来人员管理model-view
    @staticmethod
    @require_GET
    def migrant(request):
        context = {'header': '小区外来人员管理'}
        return render(request, 'common/migrant/migrant.html', context=context)

    @staticmethod
    @require_POST
    def list(request):
        migrant_list = models.Migrants.objects.all()
        data = []
        for i in migrant_list:
            data.append(model_to_dict(i))
        return JsonResponse(data, safe=False)

    @staticmethod
    @require_GET
    def add(request):
        context = {}
        return render(request, 'common/migrant/migrant_add.html', context=context)

    @staticmethod
    @require_POST
    def save(request):
        single_migrant = models.Migrants()
        m_id = request.POST['id']
        if m_id != '':
            single_migrant.id = int(m_id)
        single_migrant.name = request.POST['name']
        single_migrant.age = request.POST['age']
        single_migrant.sex = request.POST['sex']
        single_migrant.phone = request.POST['phone']
        single_migrant.bce_user_id = request.POST['bce_user_id']
        single_migrant.save()
        single_migrant = models.Migrants.objects.filter(bce_user_id=single_migrant.bce_user_id)[0]
        result = {'message': '添加成功', 'user_id': single_migrant.id, 'type': '业主', 'name': single_migrant.name}
        return JsonResponse(result)

    @staticmethod
    @require_POST
    def delete(request):
        migrant_id = request.POST['cmsMigrantId']
        single_migrant = models.Migrants.objects.filter(id=migrant_id)
        result = {'message': '', 'code': 200}
        if single_migrant.delete()[0]:
            result['message'] = '删除成功'
        return JsonResponse(result)

    @staticmethod
    @require_POST
    def update(request):
        migrant = models.Migrants()
        migrant.id = request.POST['id']
        migrant.name = request.POST['name']
        migrant.age = request.POST['age']
        migrant.sex = request.POST['sex']
        migrant.phone = request.POST['phone']
        migrant.bce_user_id = request.POST['bce_user_id']
        migrant.save()
        data = {'message': '保存成功', 'code': 200}
        return JsonResponse(data)

    @staticmethod
    @require_GET
    def edit(request):
        path = request.get_full_path()
        migrant_id = path.split('/')[-1]
        context = {}
        if migrant_id:
            single_migrant = models.Migrants.objects.get(id=migrant_id)
            context['item'] = model_to_dict(single_migrant)
        return render(request, 'common/migrant/migrant_edit.html', context=context)
