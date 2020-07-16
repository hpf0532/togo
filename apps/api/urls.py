# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/7/8 15:28
# file: urls.py
# IDE: PyCharm

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import rsa
from .views import auth
from .views import user
router = DefaultRouter()
router.register("rsas", rsa.RsaView)


urlpatterns = [
    path('login/', auth.LoginView.as_view(), name="login"),
    path('user/info/', user.UserInfoView.as_view(), name="userinfo"),
    path('', include(router.urls)),
]
