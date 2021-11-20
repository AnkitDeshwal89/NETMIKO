from netmiko import ConnectHandler
from getpass import getpass

device1= {
        "host":"192.168.129.133",
        "username":"cisco",
        "password":getpass(),
        "secret":getpass(),
        "device_type":"cisco_ios",
        "session_log":"my_session.txt",
        }

net_connect = ConnectHandler(**device1)
net_connect.enable()
command = "show run | section logging"
output1=net_connect.send_command(command)
print(output1)
#cfg = "logging buffered 20000"
output = net_connect.send_config_from_file(config_file="cfg_file.txt") 
print(output)
output1=net_connect.send_command(command)
print(output1)
net_connect.disconnect()
