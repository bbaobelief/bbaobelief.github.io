Title: Flex2 破解搜狐视频v5.0 去广告+美剧下载教程
Date: 2014-08-20 09:37:19
Category: Other
Tags: flex2, 破解
Slug: ios-flex2


由于搜狐视频版权问题，现在不能离线观看美剧，且现在ios8.3系统暂时没有人上传flex2的搜狐视频破解补丁，于是自己做了个，仅作破解记录。

#### 一、确保ios已越狱且安装了flex2

---

#### 二、去软件启动广告

搜索 LaunchAdvertItem , 找到 -(BOOL)existLaunchAdvertImage 并将其的值修改为 FALSE 即可。

---

#### 三、去除视频广告

搜索 STADPauseView , 找到 -(id)initWithFrame:(CGRect) , 将其值改为 (NULL) 。

搜索 ASAdvertPlayerViewController , 找到 -(id)advertInfo , 将其值改为 (NULL) 。

---

#### 四、去除美剧下载限制

搜索 VideoBaseInfo， 将-(BOOL)isDownloadable 的值改为 TURE 。

---

五、在flex2中启用补丁，现在就可以自由的无广告下载缓存美剧了。
