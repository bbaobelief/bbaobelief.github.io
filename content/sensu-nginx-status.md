Title: sensu插件nginx-status
Date: 2015-12-20 09:37:19
Category: Sensu
Tags: Python, sensu, sensu-plugin
Slug: sensu-nginx-status

#### 第一次写sensu的插件，暂作格式规范记录。

> 地址：[https://github.com/sensu/sensu-plugin-python](https://github.com/sensu/sensu-plugin-python)

```
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