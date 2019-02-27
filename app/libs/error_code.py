# -*- coding: utf-8 -*-
# @Time    : 18-12-24 下午3:55
# @Author  : Fuhz
# @Email   : 
# @File    : error_code.py
# ---------------------


from app.libs.errors import APIException

USER_NOT_FOUND = 1001
USER_EXISTED = 1002

errors = {
    "TooManyRequests": {
        "status": 429,
        "msg": "Too many requests"
    }
}


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class DeleteSuccess(Success):
    code = 202
    error_code = -1


class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000



class AuthFailed(APIException):
    code = 401
    msg = 'authorization failed'
    error_code = 1002


class Forbidden(APIException):
    code = 403
    msg = 'forbidden, not in scope'
    error_code = 1004


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found'
    error_code = 1001


class ServerError(APIException):
    code = 500
    error_code = 999
    msg = 'sorry, we make a mistake'
