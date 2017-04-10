Title: Centos vps安装VPN
Date: 2015-04-20 14:37:19
Category: Linux
Tags: Linux, vpn, pptp
Slug: centos-vpn


#### 一、首先检查你VPS的PPP和TUN有没有启用：
```
cat /dev/ppp   

cat /dev/net/tun
```
显示结果为：

```
cat: /dev/ppp: No such device or address

cat: /dev/net/tun: File descriptor in bad state
```
表明通过，上述两条只要有一个没通过都不行。如果没有启用，你可以给VPS提供商Submit 一个 Ticket请求开通：

> Hello   
> 
> Could you enabled TUN-TAP for me? I want run pptp-vpn on my VPS.   
> 
> Thank you.

确认 PPP 和 TUN 启用后，开始安装 ppp 和 iptables：

```
yum install -y ppp iptables
```
#### 二、安装pptp：
#### （适用32位系统）  

> rpm -ivh http://acelnmp.googlecode.com/files/pptpd-1.3.3-1.rhel4.1.i386.rpm 
#### （适用64位系统）
> rpm -ivh http://acelnmp.googlecode.com/files/pptpd-1.3.3-1.rhel4.x86_64.rpm  

#### 三、配置pptp，编辑/etc/pptpd.conf文件：

```
vim /etc/pptpd.conf
```

把下面字段前面的#去掉：

```
localip 192.168.0.1   
remoteip 192.168.0.234-238,192.168.0.245
```

#### 四、编辑/etc/ppp/options.pptpd 文件：


```
vim /etc/ppp/options.pptpd  

去掉ms-dns前面的#，并使用Google的DNS服务器，修改成如下字段：

ms-dns 8.8.8.8   

ms-dns 8.8.4.4
```

#### 五、设置VPN账号密码，编辑/etc/ppp/chap-secrets这个文件：


```
vim /etc/ppp/chap-secrets
```

#### 六、修改内核设置，使其支持转发，编辑 /etc/sysctl.conf 文件：

```
vim /etc/sysctl.conf  

将“net.ipv4.ip_forward”的值改为1，同时在“net.ipv4.tcp_syncookies = 1”前面加#
```

#### 七、使 sysctl.conf 配置文件生效并添加 iptables 转发规则：


```
sysctl -p 

iptables -t nat -A POSTROUTING -s 192.168.0.0/24 -j SNAT --to-source ***.***.***.*** (***.***.***.***为你VPS的公网IP地址)   

iptables -A POSTROUTING -t nat -s 192.168.0.0/24 -o eth0 -j MASQUERADE

iptables -A INPUT -p tcp -m state --state NEW -m tcp --dport 1723 -j ACCEPT #注：这条命令尽量放在防火墙列表前面几条不然可能会阻止  

保存iptables转发规则：

/etc/init.d/iptables save  

重启 iptables：

/etc/init.d/iptables restart  

重启pptp服务：

/etc/init.d/pptpd restart  

设置开机自动运行pptp服务：

chkconfig pptpd on  

设置开机自动运行iptables服务：

chkconfig iptables on  

到此安装配置结束了。
```
