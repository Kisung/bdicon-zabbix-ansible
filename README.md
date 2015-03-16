# bdicon-zabbix-ansible

## Overview
Automatic installation and zabbix proxy agent with anssible
Zabbix Proxy, Zabbix Agent 자동설치,설정을 위한 Playbook입니다.

## Environment
Platform : AWS
OS : Ubuntu 14.04
Zabbix-Server 2.2.2 : 통합 모니터링을 위해 미리설치됨
Zabbix-Proxy 2.2.2 : playbook을 통한 자동설치 대상
Zabbix-Agent 2.2.2 : playbook을 통한 자동설치 대상

## Requirement
`Python Zabbix API` - [zabbix](https://github.com/gescheit/scripts/tree/master/zabbix) by gescheit - a Python library (PyPI **zabbix-api**)

`Ansible` - [doc](http://docs.ansible.com/index.html) 

## Work Flow
### common
1.Hosts

   ```
localhost


```

2.variable
```
var
```

3.External Vars
```
Ext vars
```


### Zabbix Proxy
1.python-mysqldb
2.mysql-server
3.zabbix-proxy-mysql
4.Start the MySQL service
5.update mysql root password for all root accounts
6.Create database
7.Create database user localhost
8.Create database user '%'
9.Zabbix Sceme File Copy
10.Create Zabbix Scheme
11.zabbix proxy init
12.zabbix proxy config 
13.Assures /usr/lib/zabbix/externalscripts dir exists
14.restart zabbix-proxy
15.zabbix server create proxy

### Zabbix Agent


### Structure
###### Playbook
    - create-zabbix-agent.yml
    - create-zabbix-proxy.yml

###### Var
    - external_vars.yml

###### Hosts6
    - hosts

###### Template6
    - zabbix_proxy.conf.j2
    - zabbix_agentd.conf.j2
    - zabbix-proxy.j2

###### files6
    - schema.sql

###### Zabbix API Script(python)6
    - zabbix_add_proxy.py
    - zabbix_add_host.py

###### Test6
    - test-yml/








