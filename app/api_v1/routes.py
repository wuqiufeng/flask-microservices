# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.register import Register
from .api.persons import Persons


routes = [
    dict(resource=Register, urls=['/register'], endpoint='register'),
    dict(resource=Persons, urls=['/persons'], endpoint='persons'),
]