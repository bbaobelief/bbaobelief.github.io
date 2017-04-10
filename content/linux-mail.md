Title: mail命令发送邮件中文乱码或附件为tcmime.*.bin
Date: 2014-05-15 21:57:53
Category: linux
Tags: Python, Linux, 报错
Slug: linux-mail

由于公司API服务器需要统计用户访问信息，于是编写了shell脚本发送统计信息到邮箱。

但收到的邮件出现乱码，解决过程记录：

### 现象

- 使用Foxmail客户端收取邮件中文出现乱码，如“报告生成时间???2015-05-14 00:30 总???问???:515076”；
- 使用web邮箱收取邮件无内容，只显示附件为tcmime.1101.1101.4747.bin之类的内容；

### 分析

- 检查脚本文件编码是否为utf-8（可vi进去后，:set fileencoding查看）;
- 检测系统环境是否安装了中文包支持（使用 locale命令）；
- 检查shell命令行和crond环境变量是否一致（使用env查看）

### 解决

我这里的中文乱码原因是因为shell命令行和crond环境变量不一致导致，脚本中加入export LANG=en_US.UTF-8