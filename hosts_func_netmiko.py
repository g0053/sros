from netmiko import ConnectHandler
A1R1 = { 'device_type':'alcatel_sros', 'ip':'10.10.10.101', 'username':'gus', 'password':'pass'}
A1R2 = { 'device_type':'alcatel_sros', 'ip':'10.10.10.102', 'username':'gus', 'password':'pass'}
routers = [A1R1, A1R2]


def create_prefix():
 commands = ['show service service-using', 'show users']
 for ip in routers:
  print('Connection to device {}'.format(ip['ip']))
  net_connect = ConnectHandler(**ip)
  output = net_connect.send_config_set(commands)
  print(output)
 

create_prefix()




#Change show commands to any /configure ...
