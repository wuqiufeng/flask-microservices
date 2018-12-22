# -*- coding: utf-8 -*-
# @Time    : 18-12-22 上午10:00
# @Author  : Fuhz
# @Email   : 
# @File    : test.py
# ---------------------
import os

# from dotenv import load_dotenv
#
# basedir = os.path.abspath(os.path.dirname(__file__))
# load_dotenv(os.path.join(basedir, '.env'))
from config import config

SETTINGS = config["default"]