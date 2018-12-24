# -*- coding: utf-8 -*-
# @Time    : 18-12-22 下午12:46
# @Author  : Fuhz
# @Email   : 
# @File    : push_msg.py
# ---------------------
from sqlalchemy import Text, String, Integer, Column

from app.models.base import Base


class JpushMsg(Base):
    id = Column(Integer, primary_key=True)
    account = Column(String(64), nullable=False, comment="推送的账号")
    alert = Column(String(128), comment="警报")
    contents = Column(Text, nullable=False, comment="推送的内容")
    code = Column(String(32), nullable=False, comment="推送状态")
    message = Column(String(128), comment="错误原因")

    def __repr__(self):
        return '<JpushMsg {}>'.format(self.account)
