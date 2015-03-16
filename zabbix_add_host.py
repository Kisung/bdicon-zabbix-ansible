__author__ = 'sqlca'
# -*- coding: utf-8 -*-
__author__ = 'kisung.yun'
import zabbix_api
import sys

if ( len(sys.argv) < 9 ):
    print '[zabbix_url] [username] [password] [hostgroup_id] [template_id] [proxy_id] [host_name] [host_id]'
    sys.exit(1)
else:
    zabbix_url = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    hostgroup_id = sys.argv[4]
    template_id = sys.argv[5]
    proxy_id = sys.argv[6]
    host_name = sys.argv[7]
    host_ip = sys.argv[8]

# Connect to Zabbix server
z = zabbix_api.ZabbixAPI(server=zabbix_url)
z.login(user=username, password=password)

host_id = z.host.get(
    {
        "output": "extend",
        "filter": {
            "host": [host_name]
        }
    }
)

if not host_id:
    host_id = z.host.create(
        {
            'host': host_name,
            'proxy_hostid': proxy_id,
            'groups' : [{ "groupid":hostgroup_id}],
            'templates' : [{ "templateid":template_id}],
            'interfaces': [
                {
                    "type": 1,
                    "main": 1,
                    "useip": 1,
                    "ip": host_ip,
                    "dns": "",
                    "port": "10050"
                }
            ]
        }
    )
    host_id = host_id[0]['hostids']
else:
    host_id = host_id[0]['hostid']

print host_id

