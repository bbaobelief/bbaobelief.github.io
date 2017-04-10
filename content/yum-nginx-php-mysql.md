Title: yum安装PHP+Nginx+Mysql
Date: 2014-05-27 21:41:39
Category: Linux
Tags: Linux, nginx, mysql
Slug: yum-nginx-php-mysql


```
环境:Contos6.4 32位
配置：2核+512memory+30disk
```

## Step1：安装Yum源

因为nginx和php-fpm都不能直接通过Yum直接安装，所以我们需要下载两个仓库到我们的VPS上。

```
# rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
# rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm
```

报错1：

```
Error: Cannot retrieve metalink for repository: epel. Please verify its path and try again
```

处理很简单，修改文件“/etc/yum.repos.d/epel.repo”，将baseurl的注释取消，mirrorlist注释掉。即可。

报错2：

```
# yum [Errno 256] No more mirrors to try 解决方法
# yum clean all
# yum makecache
```

## Step2：安装Mysql

```
# yum install mysql mysql-server
```

安装完毕后，重启Mysql

```
# /etc/init.d/mysqld restart
```

重启完后，我们可以启动Mysql的安全配置项

```
# /usr/bin/mysql_secure_installation
```

Step3：安装nginx

```
# yum install nginx
# /etc/init.d/nginx start
```

在浏览器上直接输入ip地址测试

通过运行下面的命令来显示你服务器的ip地址。

```
ifconfig eth0 | grep inet | awk '{ print $2 }'
```

## Step4：安装php

因为php包是在REMI仓库中的，并且目前是被禁用的。我们首先要做的就是启用REMI仓库并且安装php和php-fpm还有php-mcrypt（phpmyadmin需要php-mcrypt和php-mbstring扩展，不安装可能会在启动phpmyadmin时候导致模块缺失的错误。你还可以选择安装其他所需要的扩展，已经在下面列出）。

```
# yum --enablerepo=remi,remi-php55 install php-fpm php-mysql php-mcrypt php-mbstring
```

更多扩展项如下：

```
yum --enablerepo=remi,remi-php55 install php-cli php-gd php-pear php-mysqlnd php-pdo php-pgsql php-pecl-mongo php-sqlite php-pecl-memcached php-pecl-memcache php-mbstrin php-xml php-soap php-mcrypt php-fpm
```

## Step5：配置nginx

打开默认的nginx配置文件

```
# vi /etc/nginx/nginx.conf
```

将workerprocesses的数字提升到2，保存并退出。

现在来配置nginx的虚拟主机。

```
# vi /etc/nginx/conf.d/default.conf
```

相关配置和配置改动（在配置的下面）如下。

```
server {

    listen 80;

    server_name example.com;

    location / {

         root /usr/share/nginx/html;

         index index.php index.html index.htm;

    }

    error_page 404 /404.html;

    location = /404.html {

        root /usr/share/nginx/html;

    }

    error_page 500 502 503 504 /50x.html;

    location = /50x.html {

        root /usr/share/nginx/html;

    }

    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000

    #

    location ~ \.php$ {

        root /usr/share/nginx/html;

        fastcgi_pass 127.0.0.1:9000;

        fastcgi_index index.php;

        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;

        include fastcgi_params;

    }

}
```

删除/etc/nginx/conf.d/目录下不用的配置

## Step6：配置php-fpm

打开php-fpm配置

```
# vi /etc/php-fpm.d/www.conf
```

在用户和组中，用nginx代替apache

```
user = nginx
group = nginx
```

保存并重启php-fpm。

```
# service php-fpm restart
```

## Setp7：创建phpinfo测试

首先我们创建一个新的文件。

```
# vi /usr/share/nginx/html/info.php
```

加入

```
<?php phpinfo(); ?>;
```

保存并退出。

重启nginx，使配置生效。（注：将来对配置进行任何更改后，都要重启，配置才会生效。）

访问你在配置中输入的域名或者ip地址对应的phpinfo页面。[http://IP/info.php](http://ip/info.php)

## Step8：设置自启动。

最后一步就是将刚刚装的所有程序设置自启动。

```
# chkconfig --levels 235 mysqld on
# chkconfig --levels 235 nginx on
# chkconfig --levels 235 php-fpm on
```

恭喜，你已经完成了配置部分
