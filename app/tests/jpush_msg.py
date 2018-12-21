# -*- coding: utf-8 -*-
# @Time    : 18-12-19 下午12:53
# @Author  : Fuhz
# @Email   : 
# @File    : jpush_msg.py
# ---------------------
import datetime
import jpush


class JpushNotify():
    def __init__(self, ak="977813ed9ea938e2e56c9608", secret="c23492ffbf7e3348db3be6c1"):
        self.app_key = ak
        self.master_secret = secret
        self._jpush = jpush.JPush(self.app_key, self.master_secret)
        self._jpush.set_logging("DEBUG")

    def send_notify(self, mobile, context):
        print(context)
        push = self._jpush.create_push()
        push.audience = jpush.alias(mobile)
        push.platform = jpush.all_

        # andriod_ctx=jpush.android(extras=context)
        ios_ctx = jpush.ios(extras=context, sound_disable=False)

        push.notification = jpush.notification(alert="告警通知", android={'extras': context}, ios=ios_ctx)

        response = push.send()
        print(response)


if __name__ == '__main__':
    msg = {
        "state": "1",  # state:1 报警声  #state:2 报警解除
        "time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "type": 26,  # 设备类型
        "mac": "呵呵呵呵呵呵",
        "address": "海马中心",
        "alarm_reason_id": 2,
        "alarm_reason": "哈哈哈哈哈哈哈哈哈哈",
    }

    jpntf = JpushNotify("cca17040573d18de45444b76", "99f90513247fc162f814eec3")
    jpntf.send_notify("18964035205", msg)