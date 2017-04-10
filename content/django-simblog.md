Title: django博客simblog
Date: 2013-05-01 21:49:37
Category: Django
Tags: django, Python
Slug: django-simblog


#### 概述

此博客系统基于Django-1.7.7开发而成，通过nginx+uwsgi运行于[locvps](http://my.locvps.com/page.aspx?c=referral&u=21948)(每月31元，优惠码：**mc20150325** - 仅限洛杉矶MC机房5折终身优惠)上，Python版本为 2.7.6。

功能，感谢Chopstack提供主题。

    1.文章、分类和页面的增删    
    2.文章按年、月  
    3.集成simditor富文本编  
    4.集成Prettify代码  
    5.集成多说  
    6.rss和sitemap

#### 备注

    1.为什么使用simditor而不用markdown，个人比较喜欢simditor的简洁美观，还有不习惯markdown的语法；
    2.为什么使用highlight而不用Pygments，有洁癖，不想安装第三方插件让后端程序太臃肿；
    3.为什么使用多说评论而不用django自带的评论，你会为了评论去注册帐号吗？
