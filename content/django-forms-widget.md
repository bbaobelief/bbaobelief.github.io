Title: django 自定义 forms widget属性
Date: 2015-06-27 11:37:19
Category: Django
Tags: django, Python
Slug: django-forms-widget


#### models.py


```
class Task(models.Model):
    '''任务表'''
    title = models.CharField(u'标题',max_length=30)
    description = models.TextField(u'描述')
    creator = models.ForeignKey(User, verbose_name=u'创建人')
    type = models.ForeignKey('Workorder',verbose_name=u'任务类型')
    state = models.ForeignKey('State', verbose_name=u'当前状态')
    create_time = models.DateTimeField(u'创建时间',auto_now_add=True)
    expire_Time = models.DateTimeField(u'期望时间')
    finish_time = models.DateTimeField(u'完成时间',auto_now=True)

    class Meta:
        verbose_name = u'任务创建'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __unicode__(self):
        return self.title
```

默认生成html中title input中没有size属性，是默认大小，如果自定义大小可以如下：

#### forms.py

方法1：(重写了字段，此处不推荐)


```
class TaskForm(forms.ModelForm):
    title=forms.CharField(label=u'标题0', widget=forms.TextInput(attrs={'size':'10'}))
	
    class Meta:
        model = Task
        fields = "__all__"
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
```

#### 方法2：（推荐）


```
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        # exclude = [] # uncomment this line and specify any field to exclude it from the form
        widgets = {
            'title': forms.Textarea(attrs={'cols': 20, 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
```



#### 附widgets教程：

> https://docs.djangoproject.com/en/dev/ref/forms/widgets/#module-django.forms.widgets