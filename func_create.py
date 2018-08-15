from netmiko import ConnectHandler


platform = 'alcatel_sros'
host = '10.10.10.1'
username = 'admin'
password = 'vasyapupkin1'
device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)


def create_prefix():
        device.config_mode()
        commands = ['router policy-options', 'begin', 'prefix-list TEST67 prefix 10.20.67.0/24 exact', 'commit', 'exit']
        output = device.send_config_set(commands)
        device.disconnect()
        return output

vasya = create_prefix()

print(vasya)

