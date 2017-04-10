Title: django 设置 数据库缓存
Date: 2015-03-20 10:37:19
Category: Django
Tags: django, Python
Slug: django-cache


最近博客增加了许多新功能，访问速度有所下降，故启用了django的数据库全站缓存。

Django 官方缓存系统介绍：
> https://docs.djangoproject.com/en/1.8/topics/cache/#database-caching

配置cache方式及内部实现机制：
    django中cache大体分为三种，即针对全站的缓存配置、针对视图的缓存配置、针对数据的缓存配置。本站采用数据库+全站缓存。

#### 1.设置缓存，在settings.py添加

```
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',  # 要缓存的表名
        'TIMEOUT': 600,                # 默认的缓存有效时间,以秒计. 默认值是 300 秒(五分钟).
        'OPTIONS': {
            'MAX_ENTRIES': 1000        # 缓存的最大条目数(超出该数旧的缓存会被清除,默认值是 300).
        }
    }
}
```

#### 2.创建缓存表

```
python manage.py createcachetable
```

#### 3.缓存整个站点

设置了缓存类型之后, 最简单使用缓存的方式就是缓存整个站点. 

在``MIDDLEWARE_CLASSES`` 设置中添加 django.middleware.cache.CacheMiddleware , 就象下面的例子一样:

```
MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',          # 注意位置，在前
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',       # 注意位置，在后
)
```

#### 4.在settings.py添加CACHE_MIDDLEWARE_SECONDS :每个页面应该被缓存的秒数。

```
CACHE_MIDDLEWARE_SECONDS = 500   # 每个页面应该被缓存的秒数
```

#### 5.重启django,就可以体验缓存了。