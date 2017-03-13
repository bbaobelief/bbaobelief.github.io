Title: yum安装
Date: 2013-03-03 10:15
Category: Python
Tags: pelican, publishing
Slug: yum
Author: crazygit
Summary: hello

# Bg-yum安装

{{>toc}}

[TOC]

* list
    * sublist
    * sublist
* list

```
:::python
# -*- coding: utf-8 -*-

import os
import hashlib
import socket
import re
import urllib2
import pickle
import time
from sensu_plugin import SensuPluginMetricGraphite

class NginxStatusMetrics(SensuPluginMetricGraphite):
    """
    This is a script for check nginx status     
    """
    def __init__(self):
        self.last_metrics_dir = '/tmp/.nginx_status_metrics'
        if not os.path.isdir(self.last_metrics_dir):
            os.mkdir(self.last_metrics_dir)
        super(NginxStatusMetrics, self).__init__()

    def setup(self):
        self.parser.add_argument(
            '-u',
            '--url',
            default='http://localhost/nginx_status/',
            help='nginx status url'
        )
        self.parser.add_argument(
            '-s',
            '--schema',
            default='{0}.nginx.status'.format(socket.gethostname()),
            help='metrics schema'
        )

    def _get_nginx_status(self):
        current_time = time.time()
        req = urllib2.Request(self.options.url)

        try:
            response=urllib2.urlopen(req)
        except:
            self.warning()

        res = response.read()
        pattern = re.compile(r"Active connections: (?P<activeconn>\d+)\s+"\
                              "server accepts handled requests\s+"\
                              "(?P<accepts>\d+)\s+(?P<handled>\d+)\s+(?P<requests>\d+)\s+"
                              "Reading: (?P<reading>\d+)\sWriting: (?P<writing>\d+)\s+Waiting: (?P<waiting>\d+)")
        matcher = pattern.match(res)

        if not matcher:
            self.warning()

        status = dict(
            activeconn=matcher.group('activeconn'),
            accepts=matcher.group('accepts'),
            handled=matcher.group('handled'),
            requests=matcher.group('requests'),
            reading=matcher.group('reading'),
            writing=matcher.group('writing'),
            waiting=matcher.group('waiting'),
        )

        # Write cached
        ret = dict(
            executed_time=current_time,
            status=status
        )
        pickle.dump(ret, open(self.last_metrics_file, 'w'))
        return ret

    def run(self):
        url_md5 = hashlib.md5(self.options.url).hexdigest()
        self.last_metrics_file = os.path.join(
            self.last_metrics_dir, url_md5)
        try:
            last_status = pickle.load(open(self.last_metrics_file))
        except:
            last_status = dict()
        if not last_status:
            last_status = self._get_nginx_status()
            time.sleep(1)

        current_status = self._get_nginx_status()
        interval = current_status['executed_time'] - last_status['executed_time']
        last_status = last_status['status']
        current_status = current_status['status']
        counter_map = ['accepts', 'handled', 'requests']

        for k, v in current_status.iteritems():
            if k in counter_map:
                if int(current_status[k]) > int(last_status[k]):
                    v = "%.2f" % ((int(current_status[k])-int(last_status[k]))/interval)
                    k = k + 'rate'
                    self.output("{0},type={1},url_md5={2}".format(self.options.schema, k, url_md5), v)
            else:
                self.output("{0},type={1},url_md5={2}".format(self.options.schema, k, url_md5), v)
        self.ok()

if __name__ == "__main__":
    NginxStatusMetrics()
```


### css

```
.highlight pre {
    counter-reset: linecounter;
    padding-left: 1.5em;
    border-left: 3px solid !important;
    border-left-color: #FF8000 !important;
}
.highlight pre span.code-line {
    counter-increment: linecounter;
    padding-left: 1em;
    text-indent: -1em;
    display: inline-block;
}
.highlight pre span.code-line:before {
    content: counter(linecounter);
    padding-right: 1em;
    display: inline-block;
    color: grey;
    text-align: right;
    -webkit-user-select: none;
    -khtml-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
}
```

Python test:

    :::python
    print("foo")

    
# ttttttttttttt
    
```python
print("foo")
```

Inside a list:

1. Here is some text. Let us try the ::: version of syntax highlighting.

    Only four spaces to indent:

    :::python
    print("foo")

    Using eight spaces to indent:
    
        :::python
        print("foo")

2. Now let us try the ``` version of syntax highlighting.

    Only four spaces to indent:

    ```python
    print("foo")
    ```

    Using eight spaces to indent:

        ```python
        print("foo")
        ```
    
End of test.


###  bg-release安装
```
:::bash
rpm -ivh http://repos.iduoku.cn/bg/centos/6/x86_64/bg-release-1.1-2.el6.noarch.rpm
```

### nginx安装
```
yum install bg-nginx111

#如果没有nginx
service nginx restart
#重启
service bg-nginx111 restart
```

### php安装
```
yum install bg-php52-php
yum install bg-php53-php
yum install bg-php56-php
yum install bg-php70-php

# 如果没有php
service php-fpm restart
# 重启
service bg-php56-php-fpm restart
```

### jdk安装
```
yum install bg-jdk16
yum install bg-jdk17
yum install bg-jdk18
```

### resin安装【需要先安装jdk】
```
yum install bg-resin31-resin
yum install bg-resin40-resin

# 启动
su - work
cd /home/work/opt/bg-resin版本/bin/
./httpd.sh start 或 resin.sh

#测试
curl -I http://127.0.0.1:8080/
```

### tomcat 安装
```
yum install bg-tomcat7-tomcat
yum install bg-tomcat8-tomcat

# 通用启动脚本
/etc/init.d/bg-tomcat版本-tomcat start

# 要想使用service方式启动，需要修改/etc/init.d/bg-tomcat8-tomcat 里的JAVA_HOME
service bg-tomcat版本-tomcat start

# 启动
/home/work/opt/bg-tomcat7/bin/startup.sh
#停止
/home/work/opt/bg-tomcat7/bin/shutdown.sh
#测试
curl -I http://127.0.0.1:8080/
```