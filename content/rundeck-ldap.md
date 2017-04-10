Title: rundeck整合LDAP登录
Date: 2016-05-17 18:37:19
Category: Rundeck
Tags: rundeck, linux, ldap
Slug: rundeck-ldap


#### 1.创建Active Directory组

在Active Directory中创建一个新组，命名为“op。”然后添加用户，AD组。

#### 2\. 创建jaas-activedirectory.conf文件

```
touch /etc/rundeck/jaas-activedirectory.conf
chown rundeck:rundeck /etc/rundeck/jaas-activedirectory.conf

```

vim /etc/rundeck/jaas-activedirectory.conf

##### 线上配置文件

```
multiauth {
  com.dtolabs.rundeck.jetty.jaas.JettyCachingLdapLoginModule sufficient
    debug="true"
    contextFactory="com.sun.jndi.ldap.LdapCtxFactory"
    providerUrl="ldap://IP:389"
    bindDn="cn=administrator,cn=users,dc=baidu,dc=com"
    bindPassword="密码"
    authenticationMethod="simple"
    forceBindingLogin="true"
    userBaseDn="ou=baidu,dc=baidu,dc=com"
    userRdnAttribute="sAMAccountName"
    userIdAttribute="sAMAccountName"
    userPasswordAttribute="unicodePwd"
    userObjectClass="user"
    roleBaseDn="ou=linux,dc=baidu,dc=com"
    roleNameAttribute="cn"
    roleMemberAttribute="member"
    roleObjectClass="group"
    cacheDurationMillis="300000"
    nestedGroups=true
    reportStatistics="true";

  org.eclipse.jetty.plus.jaas.spi.PropertyFileLoginModule required
    debug="true"
    file="/etc/rundeck/realm.properties";
};

```

#### 3.修改/etc/rundeck/profile

```
cp /etc/rundeck/profile /etc/rundeck/profile.bak
vim /etc/rundeck/profile
export RDECK_JVM="-Djava.security.auth.login.config=/etc/rundeck/jaas-activedirectory.conf \
    -Dloginmodule.name=multiauth

```

#### 4.创建ACL op.aclpolicy

```
/var/lib/rundeck/exp/webapp/WEB-INF/web.xml
+        <security-role>
+                <role-name>op</role-name>
+       </security-role>

```

* * *

```
touch /etc/rundeck/op.aclpolicy
chown rundeck.rundeck /etc/rundeck/op.aclpolicy

```

* * *

```
description: OP, read access
context:
  project: '.*'
for:
  resource:
    - equals:
        kind: job
      allow: [read, refresh]
    - equals:
        kind: node
      allow: [read, refresh]
  job:
    - allow: [read, run, kill]
  node:
    - allow: [read, run]
by:
  group: 'op'

---

description: OP, Read Access
context:
  application: 'rundeck'
for:
  resource:
    - equals:
        kind: system
      allow: [read]
    - equals:
        kind: project
      allow: [read]
  project:
    - match:
        name: '.*'
      allow: [read]
by:
  group: ['op']

```