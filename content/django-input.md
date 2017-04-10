Title: django input搜索提交 值不变
Date: 2014-06-20 01:37:19
Category: Django
Tags: django, Python
Slug: django-input


群友的问题：点击搜索后搜索内容不变为空，并且显示结果。

#### 解决方案：

1.先用js获取input的value值，在点击提交事件之后重写修改input 的value值为搜索内容；

2.利用django获取request的值，返回搜索条件和结果给前端页面。

**方法2实现：**

**1.编辑urls.py，添加**

```
 (r'blog/search/$', search_blog),
```

**2.编辑views.py 添加search_blog方法**

```
def search_blog(request):
    """搜索"""
    if request.method == 'POST':
        article = request.POST.get('article')
    else:
        article = u'请输入标题'
    bloglist = Article.objects.filter(title__contains = article) 
    t = get_template('search.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

```

**3.修改search.html文件为**

```
<form name="search_form" action="" method="post"> {% csrf_token %}
<input type="text" name="article" value="{{ article }}">
<input type="submit" value="搜索">
</form>
<p>结果:</p>
{{bloglist }}
```

**效果演示：**

![django input](/images/django/13c1481a-2193-11e5-af4d-8651a0f24eb4.png)