"""
WSGI config for typeidea project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# django自带,拆分settings.py后需要修改
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typeidea.settings")

# 通过读取系统环境变量中的TYPEIDEA_PROFILE控制django加载不同的settings文件,开发环境develop.py:,线上环境:product.py
profile = os.environ.get("TYPEIDEA_PROFILE", "develop")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typeidea.settings.%s" % profile)

application = get_wsgi_application()
