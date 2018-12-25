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
    code = 500
    error_code = 999
    message = 'sorry, we make a mistake'

    def __init__(self, error_code=None, message=None, code=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if message:
            self.message = message
            self.description = message
        super(APIException, self).__init__(self.message, None)


    def get_body(self, environ=None):
        body = dict(
            status=self.error_code,
            message=self.message,
            request=request.method + ' ' + self.get_url_no_param()
        )
        self.data = body

    @staticmethod
    def get_url_no_param():
        full_path = request.full_path
        main_path = full_path.split('?')
        return main_path[0]








class APIExceptionTest(HTTPException):
    code = 500
    error_code = 999
    message = 'sorry, we make a mistake'
    data = {}


    def __init__(self, message=None, code=None, error_code=None, headers=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if message:
            self.message = message
        super(APIException, self).__init__(self.message, None)

    def get_body(self, environ=None):
        body = dict(
            message=self.message,
            status=self.error_code,
            request=request.method+' '+self.get_url_no_param()
        )
        text = json.dumps(body)
        return text


    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = request.full_path
        main_path = full_path.split('?')
        return main_path[0]

