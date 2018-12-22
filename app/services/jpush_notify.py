# -*- coding: utf-8 -*-
# @Time    : 18-12-22 下午12:58
# @Author  : Fuhz
# @Email   : 
# @File    : jpush_notify.py
# ---------------------
import jpush

from app.config import Config


class JpushNotify():
    def __init__(self, ak, secret):
        self.app_key = ak if ak else Config.JPUSH_API_KEY
        self.master_secret = secret if secret else Config.JPUSH_MASTER_SECRET
        self._jpush = jpush.JPush(self.app_key, self.master_secret)
        self._jpush.set_logging("DEBUG")

    def send_notify(self, mobile, context, alert=''):
        push = self._jpush.create_push()
        push.audience = jpush.alias(mobile)
        push.platform = jpush.all_

        alert = alert if alert != '' else "告警通知"
        # andriod_ctx=jpush.android(extras=context)
        # ios_ctx = jpush.ios(extras=context, sound_disable=False)

        push.notification = jpush.notification(alert=alert, android=context, ios=context)
        try:
            response = push.send()
        except
