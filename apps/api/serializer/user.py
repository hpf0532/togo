# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/7/15 15:15
# file: user.py
# IDE: PyCharm

from rest_framework import serializers
from apps.api import models


class UserModelSerializer(serializers.ModelSerializer):
    """用户信息序列化类"""
    class Meta:
        model = models.User
        fields = ["id", "username", "avatar"]