from rest_framework import serializers

from .models import PersonalData


# 个人信息xu
class PersonalDataCommonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalData
        fields = "__all__"
