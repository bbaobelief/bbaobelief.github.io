Title: django 发送html模版渲染邮件
Date: 2015-10-15 14:57:19
Category: Django
Tags: django, Python, html模版
Slug: django-html-mail

#### 1.settings.py文件中添加配置：

```
# email config
EMAIL_HOST='smtp.163.com'
EMAIL_HOST_USER='bbaobelief@163.com'
EMAIL_HOST_PASSWORD='123456'
EMAIL_USE_TLS = True
```

#### 2.发送简单邮件：


```
from django.core.mail import send_mail

send_mail('标题','内容','bbaobelief@163.com', ['773889242@qq.com'],fail_silently=True)
```

#### 3.发送html邮件

```
#mailer.py
# -*- coding: utf-8 -*-
from django.core.mail import EmailMessage
from django.template import loader
from amms.settings import EMAIL_HOST_USER   #项目配置邮件地址，请参考发送普通邮件部分

import time

def send_html_mail(subject, content, recipient_list):
    html_content = loader.render_to_string(
                        'mail_template.html',               #需要渲染的html模板
                        {
                            'name':content['name'],
                            'date':time.strftime("%Y-%m-%d %X",time.localtime()),    #参数
                            'info':content['info']
                        }
                   )
    msg = EmailMessage(subject, html_content, EMAIL_HOST_USER, recipient_list)
    msg.content_subtype = "html" # Main content is now text/html
    msg.send()

#send_html_mail(subject, html_content, [收件人列表])
```

#### 4.html模版

```
<span style="color: rgb(255, 0, 0);"><b>你好:{{ name }}，时间：{{ date }};</b></span>
<b><font color="#ff00ff">任务：{{ info }}</font></b>

<html>
 <head></head>
 <body>
  <table cellspacing="1px" style="width: 50%; border: 1px outset rgb(128, 128, 128); border-spacing: 1px;">
   <tbody>
    <tr>
     <td style="border:1px #808080 inset;padding:1px;">申请人</td>
     <td style="border:1px #808080 inset;padding:1px;">{{ name }}</td>
    </tr>
    <tr>
     <td style="border:1px #808080 inset;padding:1px;">任务</td>
     <td style="border:1px #808080 inset;padding:1px;">{{ info }}</td>
    </tr>
    <tr>
     <td style="border:1px #808080 inset;padding:1px;">时间</td>
     <td style="border:1px #808080 inset;padding:1px;">{{ date }}<br /></td>
    </tr>
   </tbody>
  </table>
 </body>
</html>
```

#### 5.发送调用

```
from workflow.mailer import *
send_html_mail('你有待审批工单', {'name':'zheng','info':'lvs vip申请'}, ['773889242@qq.com',])
```

#### 6.效果演示

#### 7.官方文档：
> https://docs.djangoproject.com/en/1.8/topics/email/