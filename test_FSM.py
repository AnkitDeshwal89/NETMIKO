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
command = "show ip interface brief" 
output = net_connect.send_command(command,use_textfsm=True) 
print(output)
net_connect.disconnect()
