Title: lightbox2 图片放大浏览
Date: 2015-10-25 21:37:19
Category: Web
Tags: javascript, lightbox2
Slug: web-lightbox2

一直想为博客增加个图片浏览功能，今天研究了半天终于弄好啦，效果还是挺满意的。

插件用的是lightbox2：[http://lokeshdhakar.com/projects/lightbox2/](http://lokeshdhakar.com/projects/lightbox2/)

看了下说明文档，这个插件是根据**data-lightbox**属性来调用js的，但我的富文本编辑器默认不识别data-lightbox属性，保存之后会自动去掉，而且手动编辑加data-lightbox也很low。故在前端用js解决：

```
<script type="text/javascript">
$(document).ready(function() {
	//为图片添加超链接
	$(".post-content img").each(function() {
		var strA = "<a href='" + this.src + "' data-lightbox='example'></a>";
		$(this).wrapAll(strA);
	});
});
</script>
```

#### 遇到的坑：lightbox2的js文件必须放到html末尾，放到head不执行。
