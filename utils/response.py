# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/6/17 18:04
# file: response.py
# IDE: PyCharm

class BaseResponse(object):

    def __init__(self,status=True, data=None, error=None):
        self.status = status
        self.data = data
        self.error = error

    @property
    def dict(self):
        return self.__dict__