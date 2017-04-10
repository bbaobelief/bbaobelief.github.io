Title: jenkins配置Git及ssh认证
Date: 2016-06-23 19:37:19
Category: Jenkins
Tags: jenkins, git, ssh
Slug: jenkins-git-ssh

#### 安装 “Git Plugin”插件

点击系统管理->管理插件 在"可选插件"Tab里找到 Git Plugin ，安装该插件， 装完后重启， 在“已安装”Tab可找到该插件

#### Git路径设置
系统管理->系统设置-Git,配置git的路径和版本（一般不需要配置，会自动识别到）

#### 认证设置
首页->Credentials->Global credentials->Add Credentials->

- Scope:Global
- Username:jenkins (根据你的运行用户决定)
- Private Key:From the Jenkins master ~/.ssh (注意，这里用到的是私钥)


#### 生成ssh keys


```
ssh-keygen -t rsa -C "zhengfuqiang@test.com"
cat ~/.ssh/id_rsa.pub (添加到你的git里)
```

#### 新建任务

- 源码管理->Git
- Repository URL:git的ssh地址
- Credentials:jenkins (刚才创建的用户)
