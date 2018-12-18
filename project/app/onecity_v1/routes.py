# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.users import Users
from .api.persons import Persons
from .api.persons_username import PersonsUsername


routes = [
    dict(resource=Users, urls=['/users'], endpoint='users'),
    dict(resource=Persons, urls=['/persons'], endpoint='persons'),
    dict(resource=PersonsUsername, urls=['/persons/<username>'], endpoint='persons_username'),
]