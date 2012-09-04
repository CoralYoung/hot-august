#!/usr/bin/env python
# coding=utf-8

import web

web.config.debug = True

GLOBAL_PROJECT_ROOT = web.ctx.env.get('DOCUMENT_ROOT') 

GLOBAL_DB_HOST = web.ctx.env.get('DB_HOST')
GLOBAL_DB_USER = web.ctx.env.get('DB_USER')
GLOBAL_DB_PASS = web.ctx.env.get('DB_PASS')
GLOBAL_DB_PORT = web.ctx.env.get('DB_PORT')
GLOBAL_DB_NAME = web.ctx.env.get('DB_NAME')
GLOBAL_DB_CHARSET = web.ctx.env.get('DB_CHARSET')
