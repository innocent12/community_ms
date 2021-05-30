from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=16, verbose_name="用户名")
    password = models.CharField(max_length=16, verbose_name="密码")
    create_time = models.DateTimeField(default=datetime.datetime.now(), verbose_name="创建时间")

    # 序列化函数
    def serialize(self):
        return {'name': self.name, 'password': self.password,
                'id': self.id}

    # 类别名定义
    class Meta:
        verbose_name = "管理员"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0},{1},{2}'.format(self.name, self.password, self.create_time)


class Residents(models.Model):
    name = models.CharField(max_length=32, verbose_name="业主姓名")
    age = models.IntegerField(verbose_name="年龄")
    sex = models.CharField(max_length=10, verbose_name="性别")
    bce_user_id = models.CharField(max_length=32, null=True, verbose_name="百度云的人脸用户编号")
    phone = models.CharField(max_length=16, verbose_name="电话")
    address = models.CharField(max_length=64, verbose_name="居家楼栋")
    job = models.CharField(max_length=32, verbose_name="工作职位")
    log_time = models.DateTimeField(default=datetime.datetime.now(), verbose_name="登记时间")

    class Meta:
        verbose_name = "小区居民"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.__str__()


class Migrants(models.Model):
    name = models.CharField(max_length=32, verbose_name="人员姓名")
    age = models.IntegerField(verbose_name="年龄")
    sex = models.CharField(max_length=8, verbose_name="性别")
    bce_user_id = models.CharField(max_length=32, null=True, verbose_name="百度云的人脸用户编号")
    phone = models.CharField(max_length=16, verbose_name="电话")
    log_time = models.DateTimeField(default=datetime.datetime.now(), verbose_name="登记时间")

    class Meta:
        verbose_name = "外来人员"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.__str__()


class CheckLog(models.Model):
    name = models.CharField(max_length=32, verbose_name="人员姓名")
    user_id = models.IntegerField(default=0, null=True, verbose_name="人员编号")
    user_type = models.CharField(max_length=16, verbose_name="人员身份")
    temperature = models.FloatField(max_length=8, verbose_name="体温")
    sign_time = models.DateTimeField(default=datetime.datetime.now(), verbose_name="登记时间")
    matter = models.CharField(max_length=64, verbose_name="事宜")
    comment = models.TextField(max_length=256, verbose_name="备注")

    class Meta:
        verbose_name = "登记记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.__str__()
