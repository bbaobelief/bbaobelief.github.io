Title: django 报错.auditor: (fields.E304) Reverse accessor 
Date: 2015-06-20 01:37:19
Category: Django
Tags: django, Python, 报错
Slug: django-related_name


#### 今天在设计models时，一张表用到了2个ManyToManyField字段，当同步数据库时报错如下：

```
ERRORS:
workflow.Workorder.auditor: (fields.E304) Reverse accessor for 'Workorder.auditor' clashes with reverse accessor for 'Workorder.creator'.
        HINT: Add or change a related_name argument to the definition for 'Workorder.auditor' or 'Workorder.creator'.
workflow.Workorder.auditor: (fields.E304) Reverse accessor for 'Workorder.auditor' clashes with reverse accessor for 'Workorder.operator'.
        HINT: Add or change a related_name argument to the definition for 'Workorder.auditor' or 'Workorder.operator'.
workflow.Workorder.creator: (fields.E304) Reverse accessor for 'Workorder.creator' clashes with reverse accessor for 'Workorder.auditor'.
        HINT: Add or change a related_name argument to the definition for 'Workorder.creator' or 'Workorder.auditor'.
workflow.Workorder.creator: (fields.E304) Reverse accessor for 'Workorder.creator' clashes with reverse accessor for 'Workorder.operator'.
        HINT: Add or change a related_name argument to the definition for 'Workorder.creator' or 'Workorder.operator'.
workflow.Workorder.operator: (fields.E304) Reverse accessor for 'Workorder.operator' clashes with reverse accessor for 'Workorder.auditor'.
        HINT: Add or change a related_name argument to the definition for 'Workorder.operator' or 'Workorder.auditor'.
workflow.Workorder.operator: (fields.E304) Reverse accessor for 'Workorder.operator' clashes with reverse accessor for 'Workorder.creator'.
        HINT: Add or change a related_name argument to the definition for 'Workorder.operator' or 'Workorder.creator'.
```


根据报错内容得知，related_name 必须唯一，于是修改models如下


```
creator = models.ForeignKey(User, verbose_name=u'申请人')
auditor = models.ManyToManyField(User,related_name='workorder_auditor', verbose_name=u'审批人')
operator = models.ManyToManyField(User,related_name='workorder_operator', verbose_name=u'执行人')
```
