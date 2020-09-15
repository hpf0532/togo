# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/7/1 16:27
# file: rsa.py
# IDE: PyCharm

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from ..serializer.rsa import RsaModelSerializer, RsaListModelSerializer
from extensions.auth import JwtAuthorizationAuthentication

from .. import models



class RsaView(ModelViewSet):
    """密钥视图"""
    authentication_classes = [JwtAuthorizationAuthentication, ]
    queryset = models.Rsa.objects
    serializer_class = RsaModelSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = RsaListModelSerializer
        return super().list(request, *args, **kwargs)
