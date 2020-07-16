# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/7/15 15:01
# file: user.py
# IDE: PyCharm

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet

from apps.api import models
from apps.api.serializer import user


class UserInfoView(APIView):
    """用户信息接口"""
    def get(self, request, *args, **kwargs):
        userinfo = user.UserModelSerializer(instance=request.user)
        return Response(userinfo.data)