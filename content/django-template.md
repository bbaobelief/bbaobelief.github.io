Title: django1.8.2报错TemplateDoesNotEx
Date: 2014-06-04 23:02:44
Category: Django
Tags: django, Python, 报错
Slug: django-template


之前一直用django1.7版本，今天在新环境部署了django1.8,引用模版报错：

```
TemplateDoesNotExist at /cmdb/index/
```

查看官网文档找到如下解决方法：

[https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.loaders.filesystem.Loader](https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.loaders.filesystem.Loader)

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],#修改settings.py把原来的[]改为TEMPLATE_DIRS的路径
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```