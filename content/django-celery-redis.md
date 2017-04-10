Title: django+Celery+redis异步执行任务
Date: 2015-09-05 13:27:19
Category: Django
Tags: django, Python, celery
Slug: django-celery-redis



关于celery介绍请自行百度

#### 1.安装Celery
用pip或easy_install安装：

```
# pip install Celery django-celery celery-with-redis
```
#### 2.安装redis

```
# wget http://download.redis.io/releases/redis-3.0.3.tar.gz
# tar xzf redis-3.0.3.tar.gz
# cd redis-3.0.3
# make
# src/redis-server
# src/redis-cli
```

#### 3.Django设置
- a.修改settings.py

```
在INSTALLED_APPS中加入app：

INSTALLED_APPS = (
  ...
  'djcelery',
}
```
- b.添加BROKER的配置：

```
#djcelery+broker配置
import djcelery
djcelery.setup_loader()

BROKER_URL = 'redis://192.168.1.83:6379/0'
#或者
#BROKER_HOST = "192.168.1.83"
#BROKER_PORT = 6379
#BROKER_USER = ""
#BROKER_PASSWORD = ""
#BROKER_VHOST = "0"
```
#### 4. 创建数据库

```
# python manage.py syncdb   # 默认
# python manage.py migrate djcelery   #South
```

#### 5.创建一个task

```
在django app目录中创建tasks.py:

import time
from celery import task

@task()
def add(x, y):
    return x + y

@task
def sendmail(mail):
    print "++++++++++++++++++++++++++++++++++++"
    print('sending mail to %s...' % mail['to'])
    time.sleep(2.0)
    print('mail sent.')
    print "------------------------------------"
    return mail['to']
```

#### 6.开启worker


```
# python manage.py celery worker --loglevel=info
```

#### 7.执行task，调用任务


```
>>> from workflow.tasks import *
>>> sendmail.delay(dict(to='zheng@me.com'))
<AsyncResult: 694b6fa8-0545-4c22-9ba2-b77d7cbb066f>
>>> add.delay(2, 15)
<AsyncResult: 42d34419-071e-49ab-9627-45428eaaeb38>
>>> a=add.delay(1,1)
>>> a.ready()
True
>>> a.get()
2
>>> a=add.delay(10,5)
>>> a.get()
15
```

#### 8.实列


```
# views.py
from workflow.tasks import add,sendmail

def task_workorder(request, id):
    """任务添加"""
    user = request.user
    if request.method == 'POST':#提交请求时才会访问这一段，首次访问页面时不会执行
        form = TaskForm(request.POST or None, request.FILES,)
        if form.is_valid():
            print '++++++++++++++'
            print form.clean
            if request.POST.has_key('sub'):
                result=form.save(commit=False)
                result.state = 2
                result.save() # 点击提交按钮则改变状态为已提交
                sendmail.delay(dict(to='zheng@me.com'))  #申请人提交后会给审批人发邮件
            else:
                form.save()
            return HttpResponseRedirect('/workflow/sqlist/')
    else:#首次访问该url时没有post任何表单
        form = TaskForm(initial={ 'type':id, 'creator':user.id, 'state':1}) #第一次生成的form里面内容的格式
    t = get_template('workflow/add.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))
```

tasks.py
```
# tasks.py
@task
def sendmail(mail):
    print "++++++++++++++++++++++++++++++++++++"
    print('sending mail to %s...' % mail['to'])
    time.sleep(2.0)
    print('mail sent.')
    print "------------------------------------"
    return mail['to']
```
