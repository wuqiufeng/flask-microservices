# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from app.libs.error_code import DeleteSuccess, ServerError
from . import Resource
from .. import schemas


class Persons(Resource):

    def get(self):
        print(g.args)
        return ServerError()

        # return {}, 200, None