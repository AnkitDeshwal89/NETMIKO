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

mac_add=input("Enter the Mac address to be searched : ")
net_connect = ConnectHandler(**device1)
net_connect.enable()
command = "show ip arp "
output = net_connect.send_command(command,use_textfsm=True)

for x in output:
    if x['mac'] ==  mac_add:
        print("found at interface : " + x['interface'])

#print(output)
net_connect.disconnect()
