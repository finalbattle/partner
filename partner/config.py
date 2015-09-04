#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created: zhangpeng <zhangpeng1@infohold.com.cn>

import partner
import os
import yaml
import uuid
import base64
import logging
import traceback

from torweb.urls import url
from torweb.tmpl import get_environment
from torweb.config import CONFIG as CONFIGURATION
from logging.config import dictConfig

settings_path = os.path.join(partner.base_path, "settings", "dev.yaml")
CONF = CONFIG = CONFIGURATION(settings_path)

dictConfig(yaml.load(open(settings_path, 'r')))
itornado = logging.getLogger("console")
logger = logging.getLogger("file")
iError = logging.getLogger("iError")

env = get_environment(partner.__name__)

# cache = partner.cache
def get_cache():
    from torweb.cache import MemcachedCache, NullCache
    from werkzeug.contrib.cache import RedisCache
    nullcache = NullCache()
    try:
        cache_servers = CONF('MEMCACHED')
        if cache_servers:
            cache = MemcachedCache(cache_servers)
    except KeyError:
        redis_cache_host = CONF("REDIS.HOST")
        redis_cache_port = CONF("REDIS.PORT")
        if redis_cache_host and redis_cache_port:
            cache = RedisCache(redis_cache_host, redis_cache_port)
    except KeyError:
        cache = NullCache()
    return cache

cache = get_cache()

static_path = os.path.join(partner.base_path, "static")

tornado_settings = {
    "static_path": static_path,
    'cookie_secret': base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes),
    'xsrf_cookies': True,
}