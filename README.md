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
