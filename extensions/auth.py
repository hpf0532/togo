# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/7/14 10:31
# file: auth.py
# IDE: PyCharm

from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from utils.jwt_auth import parse_payload
from apps.api import models


class JwtQueryParamAuthentication(BaseAuthentication):
    """
    用户需要在url中通过参数进行传输token，例如：
    http://www.pythonav.com?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NzM1NTU1NzksInVzZXJuYW1lIjoid3VwZWlxaSIsInVzZXJfaWQiOjF9.xj-7qSts6Yg5Ui55-aUOHJS4KSaeLq5weXMui2IIEJU
    """

    def authenticate(self, request):
        token = request.query_params.get('token')
        payload = parse_payload(token)
        if not payload['status']:
            raise exceptions.AuthenticationFailed(payload)

        # request.user等于用户对象，根据payload去数据库中获取用户对象。
        user_id = payload['data'].get("id")
        user = models.User.objects.filter(id=user_id).first()

        return (user, token)


class JwtAuthorizationAuthentication(BaseAuthentication):
    """
    用户需要通过请求头的方式来进行传输token，例如：
    Authorization:jwt eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NzM1NTU1NzksInVzZXJuYW1lIjoid3VwZWlxaSIsInVzZXJfaWQiOjF9.xj-7qSts6Yg5Ui55-aUOHJS4KSaeLq5weXMui2IIEJU
    """

    def authenticate(self, request):

        # 非登录页面需要校验token
        authorization = request.META.get('HTTP_AUTHORIZATION', '')
        auth = authorization.split()
        if not auth:
            raise exceptions.AuthenticationFailed({'error': '未获取到Authorization请求头', 'status': False})
        if auth[0].lower() != 'jwt':
            raise exceptions.AuthenticationFailed({'error': 'Authorization请求头中认证方式错误', 'status': False})

        if len(auth) == 1:
            raise exceptions.AuthenticationFailed({'error': "非法Authorization请求头", 'status': False})
        elif len(auth) > 2:
            raise exceptions.AuthenticationFailed({'error': "非法Authorization请求头", 'status': False})

        token = auth[1]
        result = parse_payload(token)
        if not result['status']:
            raise exceptions.AuthenticationFailed(result)

        # 数据库获取用户对象，赋值给request.user
        user_id = result['data'].get("id")
        user = models.User.objects.filter(id=user_id).first()
        return user, token