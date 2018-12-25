# -*- coding: utf-8 -*-
# @Time    : 18-12-22 上午10:00
# @Author  : Fuhz
# @Email   : 
# @File    : test.py
# ---------------------
import json
import os

# from dotenv import load_dotenv
#
# basedir = os.path.abspath(os.path.dirname(__file__))
# load_dotenv(os.path.join(basedir, '.env'))
# from config import config

# SETTINGS = config["default"]
# import os
#
# env_dist = os.environ # environ是在os.py中定义的一个dict environ = {}
#
#
# # 打印所有环境变量，遍历字典
# for key in env_dist:
#     print(key + ":  "  + env_dist[key])

string =''' {
  "status": "error",
  "messages": ["Could not find resource or operation 'BZK1.MapServer' on the system."],
  "code": 404
}'''
print(string)
temp = json.loads(string)
print(temp['messages'])

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
        # return json.dumps(data)
        # return {"status": 200, "data": data}, 200, None
        # return ClientTypeError()
        # return {"status": 200, "data": data}, 200, None
        # return Success()
        # raise Success()
        return {"status": 200, "data": data}, 200, None
        # return {}, 200, None