# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from app.libs.error_code import ServerError, ClientTypeError
from . import Resource
from .. import schemas


class JpushMsg(Resource):

    def post(self):
        print(g.json)

        accounts = g.json["accounts"]
        contents = g.json['contents']
        alert = g.json['alert'] if "alert" in g.json else None
        #
        # jpush_client = JpushNotify()
        # for account in accounts.strip(',').split(','):
        #     jpush_client.send_notify(account, contents, alert)
        data = {
            "aaa": "hahaha",
            "bbbb": "dsdadsad"
        }
        # return {"status": 200, "data": data}, 200, None
        # raise ServiceFailure(1000, "sadhkasjhdkh")

        # raise ServerError()
        raise ClientTypeError(1002, "dsadsdada")