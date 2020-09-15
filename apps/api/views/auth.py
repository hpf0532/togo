# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/7/14 10:55
# file: auth.py
# IDE: PyCharm
import bcrypt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from apps.api import models
from utils.jwt_auth import create_token
from utils.response import BaseResponse
from extensions.auth import JwtQueryParamAuthentication, JwtAuthorizationAuthentication

from togo.settings import logger


class LoginModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["username", "password"]


class LoginView(APIView):
    # def dispatch(self, request, *args, **kwargs):
    #     super(LoginView, self).dispatch(request, *args, **kwargs)
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        """ 用户登录 """
        res = BaseResponse()

        username = request.data.get('username')
        password = request.data.get('password')
        # us = LoginModelSerializer(data=request.data)
        # if not us.is_valid():
        #     return Response(us.errors, status.HTTP_400_BAD_REQUEST)

        user = models.User.objects.filter(username=username).first()
        if not user or not bcrypt.checkpw(password.encode(), user.password.encode()):
            res.status = False
            res.error = '用户名或密码错误'
            return Response(res.dict, status.HTTP_401_UNAUTHORIZED)

        logger.info("用户{}登录成功!".format(user.username))
        token = create_token({'id':user.id, 'username': user.username})
        res.data = {
            "token": token
        }
        return Response(res.dict)




