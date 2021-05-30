import base64
import datetime
import os
import time

from aip import AipFace
import cv2

APP_ID = "24045800"
API_KEY = "QwVpMsOkbHewBRm8XY9nCEAE"
SECRET_KEY = "rLHjACnGhVbLoDGKV12GYtuviFdcZ9Ts"

client = AipFace(APP_ID, API_KEY, SECRET_KEY)


# 1.摄像头展现窗口形状配置：（方形，圆形）
# 2.
# 笔记本摄像头捕获镜头
def video_capture():
    cap = cv2.VideoCapture(0)
    while True:
        # 从摄像头读取图片
        sucess, img = cap.read()
        # 转为灰度图片
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 显示摄像头，背景是灰度。
        cv2.imshow("Face", img)
        # 保持画面的持续。
        k = cv2.waitKey(1)
        if k == 27:
            # 通过esc键退出摄像
            cv2.destroyAllWindows()
            break
        elif k == ord("s"):
            # 通过s键保存图片，并退出。
            cv2.imwrite("../../statics/images/image2.jpg", img)
            cv2.destroyAllWindows()
            break
    # 关闭摄像头
    cap.release()


# 注册人脸库
def add_user(img):
    options = {}
    options["user_info"] = "user's info"
    options["quality_control"] = "NORMAL"
    options["liveness_control"] = "LOW"
    options["action_type"] = "REPLACE"
    user_id = int(time.time())
    image_type = "BASE64"
    group = "cms"
    r = client.addUser(img, image_type, group, user_id, options)
    r['result']['user_id'] = user_id
    return r


# 删除人脸信息
def remove_user(user_id):
    options = {}
    groupId = "cms"
    userId = "user1"
    """ 调用删除用户 """
    client.deleteUser(groupId, userId);


# input:base64编码
def search_img(img):
    options = {}
    options["liveness_control"] = "LOW"
    r = client.search(img, "BASE64", "cms", options)
    # print(r)
    # none to get face_token
    if r['error_code'] == 222207:
        # t = img_handle(img)
        r = add_user(img)
        # print(r)
        r['result']['tag'] = 'add'
    elif r['error_code'] == 222202:
        r['result'] = {}
        r['result']['tag'] = 'none'
    elif r['error_code'] == 0:
        r['result']['tag'] = 'search'
    return r['result']


def init_group():
    g = client.getGroupList()
    if (len(g['result']['group_id_list']) == 0) or ("cms" not in g):
        client.groupAdd(group_id="cms")
        g = client.getGroupList()
    return g


# 识别图片或者摄像头中的人脸,并返回人脸数据
# 该数据作为身份标志保存到数据库
# return : 人脸区域base64码
def img_handle(image):
    image_type = "BASE64"
    options = {}
    options["face_field"] = "age"
    options["max_face_num"] = 2
    options["face_type"] = "LIVE"
    options["liveness_control"] = "LOW"
    # im = img2base64(image)
    """ 带参数调用人脸检测 """
    t = client.detect(image, image_type, options)
    return t


# 人脸相似度,将图片识别到的人脸数据进行处理
# 与数据库中的人脸数据进行比对，识别身份
# 初始设置相似度0.95以上则可以确认身份
# return : 相似度系数、确认结果
def reconginze(image_guest, image_origin):
    images = []
    im1 = img2base64(image_guest)
    image_guest = {"image": im1, "image_type": "BASE64",
                   "face_type": "LIVE", "quality_control": "LOW",
                   "liveness_control": "HIGH"}
    images.append(image_guest)
    im2 = img2base64(image_origin)
    image_origin = {"image": im2, "image_type": "BASE64",
                   "face_type": "LIVE", "quality_control": "LOW",
                   "liveness_control": "HIGH"}
    images.append(image_origin)
    t = client.match(images)
    print(t)


# jpg图像转二进制编码
def img2base64(img):
    im = cv2.imread(img)
    # 二进制
    res, data_encoded = cv2.imencode('.jpg', im, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
    base64_code = base64.b64encode(data_encoded)
    image = base64_code.decode()
    return image


# base64编码转jpg
def base642img(img):
    image = base64.b64decode(img)
    with open('temp.jpg', 'wb') as f:
        f.write(image)


if __name__ == '__main__':
    # root_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    # guest = os.path.abspath(os.path.join(root_path, "statics/images/image2.jpg"))
    # origin = os.path.abspath(os.path.join(root_path, "statics/images/test2.jpg"))
    # reconginze(guest, origin)
    # img_handle(guest)
    # video_capture()
    print(init_group())
