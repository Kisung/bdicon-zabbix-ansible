__author__ = 'sqlca'
# -*- coding: utf-8 -*-
__author__ = 'kisung.yun'
import zabbix_api
import sys

if ( len(sys.argv) < 5 ):
    print '[zabbix_url] [username] [password] [host_name]'
    sys.exit(1)
else:
    zabbix_url = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    host_name = sys.argv[4]

# Connect to Zabbix server
z = zabbix_api.ZabbixAPI(server=zabbix_url)
z.login(user=username, password=password)

proxy_id = z.proxy.get(
    {
        "output": "extend",
        "filter": {
            "host": [host_name]
        }
    }
)

if not proxy_id:
    proxy_id = z.proxy.create(
        {
            'host': host_name,
            'status': 5
        }
    )
    proxy_id = proxy_id[0]['proxyids']
else:
    proxy_id = proxy_id[0]['proxyid']

print proxy_id

