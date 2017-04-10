Title: Django 多对多查询
Date: 2014-11-27 16:37:19
Category: Django
Tags: django
Slug: django-m2m


### 表结构

```
class Author(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
         
class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, related_name='books')
```


### 通过Book查Author

```
b = Book.objects.get(id=1) 
b.authors.all()   # 查询id1的书籍作者
```

### 通过Author查Book

```
a = Author.objects.get(id=1)
a.book_set.all()  # 查询作者id为1的所有书籍
a.books.all()     # 通过自定义的related_name查
```
