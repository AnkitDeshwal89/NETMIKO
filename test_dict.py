from netmiko import ConnectHandler
from getpass import getpass

device1= {
        "host":"192.168.129.133",
        "username":"cisco",
        "password":getpass(),
        "secret":getpass(),
        "device_type":"cisco_ios",
        "session_log":"my_session.txt"
        }

net_connect = ConnectHandler(**device1)
net_connect.enable()
command = "delete unix:/R1-Config-3"
output = net_connect.send_command(command,expect_string=r"\?",strip_prompt=False,strip_command=False)
output += net_connect.send_command("",expect_string=r'confirm',strip_prompt=False,strip_command=False)
output += net_connect.send_command("",expect_string=r'#',strip_prompt=False,strip_command=False)
print(output)
