# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from app.services import user_service
from . import Resource
from .. import schemas


class Register(Resource):

    def post(self):
        print(g.json)
        data = user_service.create_client(query_args=g.json)

        return data

