Title: django-websocket-redis安装配置并支持中文
Date: 2016-04-08 10:30:19
Category: Django
Tags: django, Python, websocket
Slug: django-websocket-redis

1.安装redis

```
$ wget http://download.redis.io/releases/redis-3.0.7.tar.gz
$ tar xzf redis-3.0.7.tar.gz
$ cd redis-3.0.7
$ make
$ src/redis-server
```

2.安装websocket

```
# pip install django-websocket-redis
```

3.配置setting

```
INSTALLED_APPS = (
    ...
    'ws4redis',
    ...
)

# TEMPLATES 配置

'OPTIONS': {
    'context_processors': [
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
    'ws4redis.context_processors.default',
    'django.contrib.messages.context_processors.messages',
    ],
},

# WebSocket Url
WEBSOCKET_URL = '/ws/'

# WebSocket Redis
WS4REDIS_CONNECTION = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': 10,
}

WS4REDIS_EXPIRE = 3600
WS4REDIS_PREFIX = 'ws'
WSGI_APPLICATION = 'ws4redis.django_runserver.application'
WS4REDIS_HEARTBEAT = '--heartbeat--'
```

4.启动websocket(这样启动websocket和django监听同一个端口)

```
./manage.py runserver
```

5.Nginx+uwsgi运行

```
# nginx 配置文件增加
location /ws/ {
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_pass http://127.0.0.1:8888;
}

# websocket配置文件
# cat wsgi_websocket.py
import os
import gevent.socket
import redis.connection
redis.connection.socket = gevent.socket
os.environ.update(DJANGO_SETTINGS_MODULE='simblog.product_settings')
from ws4redis.uwsgi_runserver import uWSGIWebsocketServer
application = uWSGIWebsocketServer()

# uwsgi配置文件
# cat uwsgi.ini
[uwsgi]
virtualenv=/你的虚拟环境/.venv/
chdir=/你的项目路径/
module=wsgi_websocket
master=True
http-socket=127.0.0.1:8888
http-websockets=true
gevent=1000
workers=2
umask = 002
buffer-size = 32768

```

6.无法发送中文，自动断开链接

我在github提的issue：[https://github.com/jrief/django-websocket-redis/issues/180](https://github.com/jrief/django-websocket-redis/issues/180)

作者建议我升级python3.0+，我的做法是通过js转换中文为unicode字符发送，虽然不完美，但解决了我目前的问题。