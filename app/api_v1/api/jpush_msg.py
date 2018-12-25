# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class JpushMsg(Resource):

    def post(self):
        print(g.json)
        # data = {
        #     "aaa": "hahaha",
        #     "bbbb": "dsdadsad"
        # }
        return {'data': 'adsadsad'}, 200, None

        # return {}, 200, None