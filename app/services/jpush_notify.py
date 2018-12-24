# -*- coding: utf-8 -*-
# @Time    : 18-12-22 下午12:58
# @Author  : Fuhz
# @Email   : 
# @File    : jpush_notify.py
# ---------------------
import jpush
from jpush import common

from app import db
from app.config import Config
from app.models.push_msg import JpushMsg


class JpushNotify():
    def __init__(self, ak='', secret=''):
        self.app_key = ak if ak else Config.JPUSH_API_KEY
        self.master_secret = secret if secret else Config.JPUSH_MASTER_SECRET
        self._jpush = jpush.JPush(self.app_key, self.master_secret)
        self._jpush.set_logging("DEBUG")

    def send_notify(self, account, contents, alert=''):
        push = self._jpush.create_push()
        push.audience = jpush.alias(account)
        push.platform = jpush.all_

        alert = "告警通知" if not alert else alert
        # andriod_ctx=jpush.android(extras=context)
        # ios_ctx = jpush.ios(extras=context, sound_disable=False)

        jpush_msg = JpushMsg()
        jpush_msg.contents = contents
        jpush_msg.alert = alert

        push.notification = jpush.notification(alert=alert, android=contents, ios=contents)
        try:
            response = push.send()
            jpush_msg.account = account
            jpush_msg.code = 'OK'
        except common.Unauthorized:
            print("Unauthorized")
            jpush_msg.code = 'ERROR'
            jpush_msg.msg = 'Unauthorized'
            # raise common.Unauthorized("Unauthorized")
        except common.APIConnectionException:
            print("conn")
            jpush_msg.code = 'ERROR'
            jpush_msg.msg = 'conn error'
            # raise common.APIConnectionException("conn")
        except common.JPushFailure:
            jpush_msg.code = 'ERROR'
            jpush_msg.msg = 'JPushFailure'
        except:
            jpush_msg.code = 'ERROR'
            jpush_msg.msg = 'unknown error'
        db.session.add(jpush_msg)

if __name__ == '__main__':
    msg = {
        "state": "1",  # state:1 报警声  #state:2 报警解除
        # "time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "type": 26,  # 设备类型
        "mac": "呵呵呵呵呵呵",
        "address": "海马中心",
        "alarm_reason_id": 2,
        "alarm_reason": "哈哈哈哈哈哈哈哈哈哈",
    }

    # jpntf = JpushNotify("cca17040573d18de45444b76", "99f90513247fc162f814eec3")
    jpntf = JpushNotify()
    jpntf.send_notify("18964035205", msg)