# -*- coding: utf-8 -*-
# @Time    : 18-12-22 上午10:00
# @Author  : Fuhz
# @Email   : 
# @File    : test.py
# ---------------------
import json
import os
from urllib import request

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
#
# string =''' {
#   "status": "error",
#   "messages": ["Could not find resource or operation 'BZK1.MapServer' on the system."],
#   "code": 404
# }'''
# print(string)
# temp = json.loads(string)
# print(temp['messages'])

response = request.urlopen(r'http://www.baidu.com/')
page = response.read()
page = page.decode('utf-8')
print(page)