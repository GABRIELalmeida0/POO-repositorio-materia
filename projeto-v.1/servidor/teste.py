from json import loads, dumps
b = {"platform": "Linux", "platform_version": "#38~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Nov  2 18:01:13 UTC 2", "architecture": ["64bit", "ELF"], "cpu": "x86_64", "hostname": "cliente1", "ip_address": "10.25.2.38", "mac_address": "08:00:27:d4:b5:8c", "memory": {"total": 1.91, "available": 1.42, "used": 0.35}, "uptime": 0.16}

file = open('dados.json', 'r') 
file_data = file.readlines()
b = file_data

c = dumps(b)
print(type(c))
print(c)
print("-----------------------------------")
c = loads(c)
print(type(c))
print(c)

file.close()
