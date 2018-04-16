import os
import uuid

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# 图片上传
def file_extension(path):
    return os.path.splitext(path)[1]


def portrait_path(instance, filename):
    extension = file_extension(filename)
    uuid_str = uuid.uuid1()
    return 'portrait/{0}{1}'.format(uuid_str, extension)


# 加密
def ali_encrypt(item):
    # just a demo
    return item + "_encrypt"


# 解密
def ali_decrypt(item):
    # just a demo
    return item.split("_")[0]


# object
def object_getattr(obj, item):
    return object.__getattribute__(obj, item)


# 用户个人信息
class PersonalData(models.Model):
    user = models.OneToOneField(User, verbose_name="用户", related_name="personal_data", on_delete=models.CASCADE)
    portrait = models.ImageField("头像", upload_to=portrait_path, blank=True)
    address = models.CharField("住址", max_length=100, blank=True)
    github = models.URLField("Github 地址", max_length=50, blank=True)


    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息管理"

    def __str__(self):
        if not self.address:
            return "blank address."
        return self.address


