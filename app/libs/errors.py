# -*- coding: utf-8 -*-
# @Time    : 18-12-24 下午3:49
# @Author  : Fuhz
# @Email   : 
# @File    : errors.py
# ---------------------
import json

from flask import request
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 400
    error_code = 9999
    msg = 'sorry, we make a mistake'

    def __init__(self, error_code=None, msg=None, code=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        self.request = request.method + ' ' + self.get_url_no_param()
        super(APIException, self).__init__(self.msg, None)


    @staticmethod
    def get_url_no_param():
        full_path = request.full_path
        main_path = full_path.split('?')
        return main_path[0]

