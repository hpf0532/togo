# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/7/14 17:46
# file: user.py
# IDE: PyCharm

import os
import bcrypt
# 加载Django环境，books_management_system是我的Django项目名称
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'togo.settings')
# 引入Django模块
import django

# 初始化Django环境
django.setup()

from apps.api import models

user = models.User.objects.create(username="admin")


user.password = bcrypt.hashpw("passw0rd123".encode(), bcrypt.gensalt()).decode()
user.save()