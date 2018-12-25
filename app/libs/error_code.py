# -*- coding: utf-8 -*-
# @Time    : 18-12-24 下午3:55
# @Author  : Fuhz
# @Email   : 
# @File    : error_code.py
# ---------------------

# Flask_limiter
from app.libs.errors import APIException

errors = {
    "TooManyRequests": {
        "status": 429,
        "message": "Too many requests"
    }
}


class ServerError(APIException):
    code = 500
    error_code = 999
    message = 'sorry, we make a mistake'


class ClientTypeError(APIException):
    code = 400
    message = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    message = 'invalid parameter'
    error_code = 1000


class NotFound(APIException):
    code = 404
    message = 'the resource are not found'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    message = 'authorization failed'
    error_code = 1002


class Forbidden(APIException):
    code = 403
    message = 'forbidden, not in scope'
    error_code = 1004