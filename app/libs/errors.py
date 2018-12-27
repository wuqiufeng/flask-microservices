# -*- coding: utf-8 -*-
# @Time    : 18-12-24 下午3:49
# @Author  : Fuhz
# @Email   : 
# @File    : errors.py
# ---------------------
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 500
    error_code = 999
    msg = 'sorry, we make a mistake'

    def __init__(self, msg=None, code=None, error_code=None, headers=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        super(APIException, self).__init__(self.msg, None)

