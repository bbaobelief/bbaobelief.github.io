Title: nginx+uwsgi部署
Date: 2015-08-12 12:30
Category: Linux
Tags: django, Python, nginx
Slug: uwsgi-nginx


#### 1. 安装必要的开发包


```
#  yum install python-devel libxml2-devel python-setuptools zlib-devel wget pcre-devel gcc make
```

#### 2. 安装nginx 


```
# useradd www
# wget http://nginx.org/download/nginx-1.6.1.tar.gz
#  ./configure --user=www --group=www \
--prefix=/usr/local/nginx \
--with-http_stub_status_module \
--with-http_gzip_static_module
//此处在本环节只需指定一个路径
# make && make install
# /usr/local/nginx/sbin/nginx      //启Nginx
```

#### 3.安装uwsgi


```
# wget http://projects.unbit.it/downloads/uwsgi-2.0.6.tar.gz
# tar -zxvf uwsgi-2.6.tar.gz 
# cd uwsgi-2.6.tar.gz 
# python setup.py build 
# make 
# mv uwsgi /usr/bin/           //将编译好的文件移动到此处
```

#### 4.测试uwsgi

在你的机器上写一个test.py


```
def application(env, start_response):
        start_response('200 OK', [('Content-Type','text/html')])
        return "Hello World"
```

然后执行shell命令：


```
# uwsgi --http :9000 --wsgi-file test.py    #注意--http :9000之间有空格
```

访问网页：

http://127.0.0.1:9001/

看在网页上是否有Hello World

#### 5.配置nginx


```
vim /usr/local/nginx/conf/nginx.conf 

    server {
        listen 80;
        server_name localhost;
        #charset koi8-r;
        access_log logs/access.log;
        error_log logs/error.log;
        location / {
            uwsgi_pass 127.0.0.1:9001;
            include uwsgi_params;
        }
        #error_page 404 /404.html;
        # redirect server error pages to the static page /50x.html
        #
        error_page 500 502 503 504 /50x.html;
        location = /50x.html {
            root html;
        }
        location /static/ {
            alias /data/www/django/mysite/aceadmin/static/;
            index index.html index.htm;
        }
        location /media/ {
            alias /data/www/django/mysite/aceadmin/media/;
        }
    }
```

#### 6.配置django

> NOTE：请保证你的django项目是正常使用的。可以使用

```
python manage.py runserver 0.0.0.0:8002
```

来测试一下你的django项目是否能正常跑起来。


```
# cat django_wsgi.py
#!/usr/bin/env python
# coding: utf-8
import os
import sys
 
# 将系统的编码设置为UTF8
#reload(sys)
#sys.setdefaultencoding('utf8')
 
#注意："mysite.settings" 和项目文件夹对应。
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")

from django.core.wsgi import get_wsgi_application 
application = get_wsgi_application()
连接django和uwsgi，实现简单的WEB服务器。
```


然后，就可以执行以下命令：


```
# uwsgi --http :9001 --chdir /data/www/django/mysite --module django_wsgi
```

这样，你就可以在浏览器中访问你的Django程序了。所有的请求都是经过uwsgi传递给Django程序的。

#### 7.配置uWSGI

新建一个XML文件：

vim uwsgi.xml，将它放在 mysite 目录下：

```
<uwsgi>
    <socket>127.0.0.1:9001</socket> <!-- 和nginx中定义的要一致 -->
    <chdir>/data/django/myblog</chdir>      <!-- 你django的项目目录 -->
    <module>django_wsgi</module> <!-- 名称为刚才上面定义的py文件名 -->
    <processes>4</processes> <!-- 进程数 -->
    <daemonize>/data/django/myblog/log/uwsgi.log</daemonize>
</uwsgi>
```

在上面的配置中，我们使用 uwsgi.log 来记录日志，开启4个进程来处理请求。

这样，我们就配置好uWSGI了。

启动uWSGI服务器

```
# cd/data/www/django/mysite
# uwsgi -x uwsgi.xml
```


在上面的设置后，可以让Nginx来处理静态文件(/static/ 和 /media/ ）。非静态文件请求Nginx会发给 socket 9001，然后让uWSGI来进行处理。

#### 8.其他设置

a.关闭django调试模式
DEBUG = False

b.复制admin文件样式
1. 修改settings.py中STATIC_ROOT为你的static静态文件的物理路径

2. 复制静态文件


```
# python manage.py collectstatic
```


3. 修改Nginx配置


```
location /static {
      root /home/user/www;
  }
```

完成上面三步后，重新加载相应设置：

重启uwsgi和nginx