from netmiko import ConnectHandler,file_transfer
from getpass import getpass

device1= {
        "host":"192.168.129.133",
        "username":"cisco",
        "password":getpass(),
        "secret":getpass(),
        "device_type":"cisco_ios",
        "session_log":"my_session.txt",
        }

source_file = "README.md"
dest_file = "README.md"
direction = "put"
file_system = "unix:"


net_connect = ConnectHandler(**device1)
net_connect.enable()
command = "dir unix:"
output1=net_connect.send_command(command)
print(output1)
ssh_conn = net_connect
transfer_dict = file_transfer(
        ssh_conn,
        source_file=source_file,
        dest_file=dest_file,
        file_system=file_system,
        direction=direction,
        overwrite_file=True,
        )
print(transfer_dict)

net_connect.disconnect()
