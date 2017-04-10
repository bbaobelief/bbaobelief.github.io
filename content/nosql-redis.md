Title: redis3.0.2 主从搭建
Date: 2014-06-18 19:03:57
Category: Linux
Tags: Linux, nosql, redis
Slug: nosql-redis


#### 环境介绍

- os： centos 6.4 x64位系统 
- master: 192.168.1.83
- slave: 192.168.1.84

## 两台机器安装redis ###

#### 安装redis组件tcl

```
# yum install tcl-devel.x86_64 tcl.x86_64 gcc
```

#### 安装redis

```
# tar zxvf redis-3.0.2.tar.gz
# make PREFIX=/usr/local/redis install
# make MALLOC=libc  #若报错执行
```

#### 生成配置

```
# /root/soft/redis-3.0.2/utils/install_server.sh
# vim /etc/redis/6379.conf # 修改
daemonize yestimeout 500
logfile /data/redis/6379/log/redis_6379.log
dir /data/redis/6379/data
```

#### 创建目录

```
# mkdir /data/redis/6379/{data,log} -p
```

#### 启动命令

```
# ln -s /usr/local/redis/bin/* /usr/bin/# mv /etc/init.d/redis_6379 /etc/init.d/redis
```

#### 启动redis

```
# service redis start
```

#### 查看端口

```
# netstat -tunpl|grep redis
```

## slave服务器配置修改 ##

```
# vim /etc/redis/6379.conf
```

#### 在以下位置添加一行

```
# slaveof
slaveof 192.168.1.83 6379
```

#### 重启redis

```
# service redis restart
```

#### 查看端口

```
# netstat -tunpl|grep redis
```

## 测试主机数据同步 ##

#### 在master主机写入key

```
[root@localhost redis]# redis-cli
127.0.0.1:6379> set name zheng
OK
127.0.0.1:6379> keys *
1) "name"
```

#### 在slave主机查看key

```
[root@localhost conf]# redis-cli
127.0.0.1:6379> keys *
1) "name"
127.0.0.1:6379>set name zheng   #默认是读写分离的
(error) READONLY You can't write against a read only slave.
```

##########主从切换##########

#### 1.停止master

```
[root@localhost redis]# service redis stop 
Stopping ...
Redis stopped
[root@localhost redis]# redis-cli 
Could not connect to Redis at 127.0.0.1:6379: Connection refused
not connected> 
```

#### 2.将从redis设成主redis

```
[root@localhost ~]# redis-cli -p 6379 slaveof NO ONE 
OK
```

#### 3.测试从redis是否切换从主redis

```
[root@localhost ~]# redis-cli 
127.0.0.1:6379> set name zhengfuqiang
OK
```

原来的主redis恢复正常了，要重新切换回去

#### 1.将现在的主redis的数据进行保存

```
[root@localhost ~]# redis-cli 
127.0.0.1:6379> set name zhengfuqiang
OK
127.0.0.1:6379> set age 24
OK
127.0.0.1:6379> set email zheng@qq.com
OK
127.0.0.1:6379> save
OK
```

#### 2.将现在的主redis根目录下dump.rdb文件拷贝覆盖到原来主redis的根目录

```
# scp /data/redis/6379/data/dump.rdb root@192.168.1.83:/data/redis/6379/data/
```

#### 启动原来的master

```
[root@localhost data]# service redis start
Starting Redis server...
[root@localhost data]# redis-cli
127.0.0.1:6379>  keys *
1) "pass"
2) "name"
3) "age"
127.0.0.1:6379> 
[root@localhost data]# redis-cli slaveof 192.168.1.83 6379#在slave切换
OK
[root@localhost data]# redis-cli
127.0.0.1:6379>  keys *
1) "name"
2) "pass"
3) "age"
4) "email"
```
