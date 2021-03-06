#!/usr/bin/env python
# coding=utf-8

import web
from config.Urls import *
from config.Settings import *

#init web.py
if web.config.get('_app') is None:
	app = web.application(urls, globals())
	web.config._app = app
else:
	app = web.config._app

#init session
if web.config.get('_session') is None:
	session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'login':False})
	web.config._session = session
else:
	session = web.config._session

#init render
if web.config.get('_render') is None:
	render = web.template.render(GLOBAL_PROJECT_ROOT + '/templates/', base = 'TLayout', globals = {'ctx':web.config._session, 'client':web.ctx, 'hasattr':hasattr})
	web.config._render = render
else:
	render = web.config._render

db = web.database(dbn='mysql', user=GLOBAL_DB_USER, pw=GLOBAL_DB_PASS, host=GLOBAL_DB_HOST, port=GLOBAL_DB_PORT, db=GLOBAL_DB_NAME, charset=GLOBAL_DB_CHARSET, use_unicode=0)

