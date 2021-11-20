from netmiko import ConnectHandler
from getpass import getpass

device1= {
        "host":"192.168.129.133",
        "username":"cisco",
        "password":getpass(),
        "secret":getpass(),
        "device_type":"cisco_ios",
        "session_log":"my_session.txt",
        #"global_delay_factor": 2,                       #global_delay_factor : waits for sometime before running command , as some clis takes time to login or show prompt
        }

net_connect = ConnectHandler(**device1)
net_connect.enable()
command = "show ip interface brief" 
output = net_connect.send_command(command,delay_factor=5)  # delay_factor is specific to command compare to global delay which is global to all command , here this specific command would take 5 second delay
print(output)
