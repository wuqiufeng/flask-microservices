# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class Persons(Resource):

    def get(self):
        print(g.args)

        return {'data':'adsadsad'}, 200, None

    def post(self):
        print(g.json)

        return {}, 204, None