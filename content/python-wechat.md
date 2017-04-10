Title: python版微信企业号发送报警信息
Date: 2013-05-06 00:25:50
Category: Python
Tags: Python
Slug: python-wechat


今天在群里看到有人问：微信如何发送报警信息，自己简单看了下。

### 注册体验号
> 地址：[http://qydev.weixin.qq.com/try?t=experience](http://qydev.weixin.qq.com/try?t=experience)进行注册操作，默认有90天的期限。

```
# -*- coding: utf-8 -*-

import sys
import urllib2
import json

reload(sys)
sys.setdefaultencoding('utf-8')

class Token(object):
    '''微信接口发送消息'''
    def __init__(self, corp_id, corp_secret):
        self.corp_id = corp_id
        self.corp_secret = corp_secret
        self.baseurl = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={0}&corpsecret={1}'.format(self.corp_id, self.corp_secret)
        self.send_values = {}

    #获取AccessToken
    def get_token(self):
        request = urllib2.Request(self.baseurl)
        try:
            response = urllib2.urlopen(request, timeout=10)
        except urllib2.HTTPError as e:
            print e.code
        token_data = response.read().strip()
        token_json = json.loads(token_data)
        if 'errcode' in token_json.keys():
            print token_json['errmsg']
            sys.exit(1)
        self.access_token = token_json['access_token']
        return self.access_token

    #发送消息
    def send_data(self,message):
        self.message = message
        self.send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + self.access_token
        self.send_values = {
           "touser": "@all",
           "msgtype": "text",
           "agentid": "2",
           "text": {
               "content": message
           },
           "safe":"0"
        }
        send_data = json.dumps(self.send_values,ensure_ascii=False)
        send_request = urllib2.Request(self.send_url, send_data)
        response = urllib2.urlopen(send_request)
        # 返回微信公共平台的信息
        msg = response.read()
        print msg

corpid = '你的corpid'
corpsecret = '你的corpsecret'
message =" [擦汗][擦汗] Nagios 警报 [擦汗][擦汗] \n\n类型 : RECOVERY \n主机 : web-001\n状态 : UP\n地址 : 192.168.1.1\n日志 : OK - load average: 0.00, 0.00, 0.00\n\n时间 : Mon May 5 15:10:18 CST 2015 \n"

get_test = Token(corpid,corpsecret)
get_test.get_token()
msg = get_test.send_data(message)

```

### 演示效果

![test wechat](/images/python/8931c31a-2191-11e5-af4d-8651a0f24eb4.png)
