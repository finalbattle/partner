#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created: zhangpeng <zhangpeng1@infohold.com.cn>

import os
import partner
import logging
import tornado.web
from tornado.options import options
from torweb.application import make_application 
from torweb.config import CONFIG
from torweb import run_torweb
from code import interact
from partner.config import logger, settings_path, tornado_settings
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


logger.info("^_^")
logger.info(settings_path)

CONF = CONFIG(settings_path)
debug = CONF("DEBUG_PAGE")
url_root = CONF("URL_ROOT")

default_port = 8888
app = make_application(partner, debug, wsgi=True, settings_path=settings_path, url_root=url_root, **tornado_settings)
setattr(app, '_wsgi', False)
if options.cmd == "runserver":
    run_torweb.run(app, port=default_port)
else:
    run_torweb.show_urls(partner)
