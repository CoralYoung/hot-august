#!/usr/bin/env python
#coding:utf-8

import web 
from config.Runtime import *
from config.Settings import *

if __name__ == "__main__":
	web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
	app.run()
