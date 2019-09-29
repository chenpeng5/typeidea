from .base import *  # NOQA
# # NOQA告诉PEP 8 规范检查工具,这个地方不需要检查,或者在文件的第一行增加# flake8: NOQA


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}