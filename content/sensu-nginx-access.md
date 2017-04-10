Title: sensu插件nginx-access
Date: 2015-12-25 10:37:19
Category: Sensu
Tags: Python, sensu, sensu-plugin
Slug: sensu-nginx-access

sensu日志分析插件。

nginx日志格式：

```
# -*- coding: utf-8 -*-

import os
import time
import json
import socket
import hashlib
from collections import defaultdict
from sensu_plugin import SensuPluginMetricGraphite

class NginxAccessMetrics(SensuPluginMetricGraphite):
    """
    This is a script for check nginx access 
    """
    def __init__(self):
        self.last_metrics_dir = '/tmp/.nginx_access_metrics'
        if not os.path.isdir(self.last_metrics_dir):
            os.mkdir(self.last_metrics_dir)
        super(NginxAccessMetrics, self).__init__()

    def setup(self):
        self.parser.add_argument(
            '-l',
            '--log',
            required=True,
            help='nginx access log'
        )
        self.parser.add_argument(
            '-s',
            '--schema',
            default='{0}.nginx.access'.format(socket.gethostname()),
            help='metrics schema'
        )

    def _get_offset_db(self):
        _db_file = os.path.join(
            self.last_metrics_dir, '.' + hashlib.md5(self.options.log).hexdigest())
        self.offset_db = _db_file

    def _get_offset(self):
        _ret = {
            'path': self.options.log,
            'inode': 0,
            'offset': 0
        }
        if os.path.isfile(self.offset_db):
            _offset_info = open(self.offset_db, 'r').read().strip().split()
            if len(_offset_info) == 3:
                _ret['inode'] = int(_offset_info[1])
                _ret['offset'] = int(_offset_info[2])
        return _ret

    def _write_offset(self, inode, offset):
        with open(self.offset_db, 'w') as fd:
            fd.write('{0} {1} {2}'.format(self.options.log, inode, offset))

    def _get_timestamp(self, time_str):
        ctime = time_str.split('+')[0]
        return time.mktime(time.strptime(ctime,'%Y-%m-%dT%H:%M:%S'))

    def _get_log_fds(self, inode, offset):
        _ret = []
        if inode == 0:
            inode = os.stat(self.options.log).st_ino
            fd = open(self.options.log, 'r')
            _ret.append((fd, inode))
        else:
            if os.stat(self.options.log).st_ino == inode:
                fd = open(self.options.log, 'r')
                fd.seek(offset)
                _ret.append((fd, inode))
            else:
                # Log rotate?
                log_dir = os.path.dirname(os.path.abspath(self.options.log))
                for _each in os.listdir(log_dir):
                    _each = os.path.join(log_dir, _each)
                    if os.stat(_each).st_ino == inode:
                        fd = open(_each, 'r')
                        fd.seek(offset)
                        _ret.append((fd, inode))
                        break
                # Add new log fd
                inode = os.stat(self.options.log).st_ino
                fd = open(self.options.log, 'r')
                _ret.append((fd, inode))
        return _ret

    def run(self):
        bandwidth = 0
        start_time = None
        end_time = None
        domain_map = defaultdict(dict)
        self._get_offset_db()
        current_offset = self._get_offset()
        fds = self._get_log_fds(current_offset['inode'], current_offset['offset'])

        for _each_fd, _each_ino in fds:
            for eachLine in _each_fd:
                try:
                    json_Line = json.loads(eachLine.decode('unicode-escape'), strict=False) 
                    if start_time == None:
                        start_time = json_Line['@timestamp']
                        end_time = json_Line['@timestamp']
                    if start_time > json_Line['@timestamp']:
                        start_time = json_Line['@timestamp']
                    elif end_time < json_Line['@timestamp']:
                        end_time = json_Line['@timestamp']
                    domain = json_Line['@fields']['host']
                    status_code = int(json_Line['@fields']['status'])
                    bits_sent = int(json_Line['@fields']['bytes_sent']) * 8
                except Exception:
                    continue
                if domain not in domain_map:
                    domain_map[domain].update(dict(
                        status=defaultdict(int),
                        bandwidth=0
                    ))
                domain_map[domain]['status']['total'] += 1
                domain_map[domain]['status'][status_code] += 1
                domain_map[domain]['bandwidth'] += bits_sent

        if start_time and end_time:
            start_time = self._get_timestamp(start_time)
            end_time = self._get_timestamp(end_time)
            end_time += 1
            interval = end_time - start_time
        # # Write offset
        self._write_offset(_each_ino, _each_fd.tell())

        if domain_map:
            for domain, info in domain_map.iteritems():
                for status_code, status_value in info['status'].iteritems():
                    self.output("{0},domain={1},type=status_code,staut_code={2}".format(
                        self.options.schema, domain, status_code), status_value/interval)
                self.output("{0},domain={1},type={2}".format(
                    self.options.schema, domain, 'bandwidth'), info['bandwidth']/interval)
        self.ok()

if __name__ == "__main__":
    NginxAccessMetrics()

```