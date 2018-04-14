from django.shortcuts import render
from rest_framework import generics, permissions

from .models import (PersonalData, )
from .serializers import PersonalDataCommonSerializer


# Create your views here.


# 添加个人信息
class AddPersonalData(generics.CreateAPIView):
    """
    :param portrait 头像
    :param address 住址
    :param github github地址
    :param user 当前信息的所有人
    """
    queryset = PersonalData.objects.all()
    serializer_class = PersonalDataCommonSerializer
    permission_classes = ()


# 获取个人信息
class RetrievePersonalData(generics.RetrieveAPIView):
    queryset = PersonalData.objects.all()
    serializer_class = PersonalDataCommonSerializer
    permission_classes = ()

    def get_object(self):
        return PersonalData.objects.get(user=self.request.user)
