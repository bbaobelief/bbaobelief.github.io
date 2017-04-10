Title: duxcms 开启nginx伪静态
Date: 2015-07-10 01:37:19
Category: Django
Tags: django, Python
Slug: duxcms-nginx


#### 今天部署了duxcms，想用来做移动端文章展示用，对默认生成的文章url不胜满意，找了下官方的资料没发现nginx的伪静态规则，于是自己写了个。

后台———系统———系统设置———性能设置———伪静态（开启）

#### nginx加入伪静态规则

```
rewrite ^(.*)/article/([0-9]+).html$ $1/index.php?r=article/Content/index&content_id=$2 last;
```

#### 补充官方方式：

```
location / {
        try_files $uri $uri/ /index.php?$args;
}
```

