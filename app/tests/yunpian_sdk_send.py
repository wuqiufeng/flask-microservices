# -*- coding: utf-8 -*-
# @Time    : 18-12-28 下午3:56
# @Author  : Fuhz
# @Email   : 
# @File    : yunpian_sms.py
# ---------------------
from yunpian_python_sdk.model import constant as YC
from yunpian_python_sdk.ypclient import YunpianClient
import urllib.parse


YUNPIAN_AK = "3dd31dd63fe4a849f9576531af5633db"


# tplvalue=urlencode(urlencode("#code#") + "=" + urlencode("1234") + "&amp;" +
#         urlencode("#company#") + "=" + urlencode("云片网"));

# 初始化client, apikey作为所有请求的默认值
client = YunpianClient(apikey=YUNPIAN_AK)
# code = '湖北省'
# app = 'Buggg'

value= {'#name#': '万达广场', '#code#': '1234湖北汉川'}
tpl_value = urllib.parse.urlencode(value)   # 注意此处不要用sdk中的解码方法，超级傻逼
# code 和 app是你模版里面的变量，我们使用py3的urllib.parse.urlencode方法对此参数进行转码，注意在｛｝中，需要在模版变量前后加上#，不然会返回参数不正确
param = {YC.MOBILE: '18964035205', YC.TPL_ID: 2531838, YC.TPL_VALUE: tpl_value}
r = client.sms().tpl_single_send(param)
print(r.msg())
print("11111111111111111")