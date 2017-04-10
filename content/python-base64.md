Title: python转换MP3文件为base64编码
Date: 2014-07-27 13:39:49
Category: Python
Tags: python,fartscroll.js
Slug: python-base64
Author: zheng

最近看到一个好玩的js库**[fartscroll.js](http://code.onion.com/fartscroll.js)**，可以让你页面每下拉一点就听到一声屁响。于是研究了一下工作原理：

滚动后向 HTML 文档中添加了 audio 元素，并且使用base64编码。使用 base64 编码的方式，避免了加载外部的音频资源。

演示地址：[http://www.opdev.cn/admin/](http://www.opdev.cn/admin/)

想自定义声音，怎么转换为Base64编码？

## 用python获得Base64编码后的字符串:

```
import base64
f=open(r'/tmp/Teemo.mp3','rb') #二进制方式打开MP3文件
mp3=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
print mp3
f.close()
```