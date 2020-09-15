# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/7/9 11:36
# file: rsa.py
# IDE: PyCharm
from rest_framework import serializers
from django.forms.models import model_to_dict
from .. import models


class RsaModelSerializer(serializers.ModelSerializer):
    switch = serializers.SerializerMethodField()
    class Meta:
        model = models.Rsa
        fields = ["id", "status", "user", "name", "private_key", "switch"]
        # 定义只在验证时用到的字段
        extra_kwargs = {'status': {'write_only': True}}

        # fields = "__all__"

    def get_switch(self, obj):
        return {"code": obj.status, "text": obj.get_status_display()}

class RsaListModelSerializer(RsaModelSerializer):
    class Meta:
        model = models.Rsa
        fields = ["id", "status", "user", "name", "switch"]
        extra_kwargs = {'status': {'write_only': True}}