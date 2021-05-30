from django.views.decorators.http import require_GET, require_POST
from app_cms.face_authencation import processor
from app_cms import models
from django.http import JsonResponse
from django.shortcuts import render


# 启用摄像头
@require_GET
def face_reconginze(request):
    processor.video_capture()
    context = {}
    return JsonResponse(context)


# 打开人脸识别界面
@require_GET
def face_video(request):
    context = {"header": "人脸识别验证"}
    return render(request, "common/checklog/face.html", context)


# 人脸图像处理
# 直接注册后的bce_user_id
@require_POST
def solve_face(request):
    # solve the image
    img_64 = request.POST.get("image")
    img_64 = img_64.split(',')[1]
    data = {}
    # search image in the dataset
    # condition
    result = processor.search_img(img_64)
    # processor.base642img(img_64)
    # exist to record temperature
    if result is not None and result['tag'] == 'search':
        bce_user_id = result['user_list'][0]['user_id']
        if models.Migrants.objects.filter(bce_user_id=bce_user_id):
            m = models.Migrants.objects.get(bce_user_id=bce_user_id)
            data['message'] = '外来人员'
            data['user_id'] = m.id
            data['name'] = m.name
            data['sex'] = m.sex
            data['phone'] = m.phone
            data['user_type'] = '其他'
        elif models.Residents.objects.filter(bce_user_id=bce_user_id):
            resident = models.Residents.objects.get(bce_user_id=bce_user_id)
            data['user_id'] = resident.id
            data['address'] = resident.address
            data['phone'] = resident.phone
            data['sex'] = resident.sex
            data['name'] = resident.name
            data['message'] = '业主'
            data['user_type'] = resident.job
            temp = models.CheckLog.objects.filter(user_id=resident.id)
            if len(temp) == 0:
                data['temperature'] = '没有记录'
            else:
                data['temperature'] = temp[0].temperature
        else:
            # 删除未注册用户人脸信息
            data['message'] = '人员登记'
            data['bce_user_id'] = bce_user_id
    elif result['tag'] == 'add':
        # none to register user
        data["bce_user_id"] = result['user_id']
        data['message'] = '人员登记'
    else:
        data["message"] = '照片不合格'
        data["code"] = 202
    return JsonResponse(data, safe=False)



