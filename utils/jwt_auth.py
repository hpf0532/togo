# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/7/14 9:50
# file: jwt_auth.py
# IDE: PyCharm
import jwt
import datetime
from jwt import exceptions

from togo.settings import JWT_EXPIRE, JWT_SALT

def create_token(payload, timeout=JWT_EXPIRE):
    """
    :param payload:  例如：{'user_id':1,'username':'wupeiqi'}用户信息
    :param timeout: token的过期时间，默认8小时
    :return:
    """
    headers = {
        'typ': 'jwt',
        'alg': 'HS256'
    }
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(hours=timeout)
    result = jwt.encode(payload=payload, key=JWT_SALT, algorithm="HS256", headers=headers).decode('utf-8')
    return result


def parse_payload(token):
    """
    对token进行和发行校验并获取payload
    :param token:
    :return:
    """
    result = {'status': False, 'data': None, 'error': None}
    try:
        verified_payload = jwt.decode(token, JWT_SALT, True)
        result['status'] = True
        result['data'] = verified_payload
    except exceptions.ExpiredSignatureError:
        result['error'] = 'token已失效'
    except jwt.DecodeError:
        result['error'] = 'token认证失败'
    except jwt.InvalidTokenError:
        result['error'] = '非法的token'
    return result


if __name__ == '__main__':
    token = create_token({"username": "admin", "id": 1})
    print(token)

    r = parse_payload(token)
    print(r)