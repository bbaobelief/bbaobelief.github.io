Title: Django1.8 安装Django-Debug-Toolbar
Date: 2015-11-28 15:37:19
Category: Django
Tags: django, Python, Toolbar
Slug: django-debug-toolbar

##### 网上很多资料都是django1.4下的，无法正常显示toolbar。

> 地址：[https://github.com/django-debug-toolbar/django-debug-toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar)

#### 安装

```
# pip install django-debug-toolbar
```

#### 设置settings.py

```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'debug_toolbar',
)
```
#### 设置MIDDLEWARE_CLASSES

```
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)
```
#### 设置Debug_Show

```
#Debug_Toolbar
def show_toolbar(request):
    print request.user
    return True

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'simblog.settings.show_toolbar',
    'JQUERY_URL': '//code.jquery.com/jquery-1.11.2.min.js',
}
```
