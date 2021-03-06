from netmiko import ConnectHandler
from getpass import getpass
net_connect = ConnectHandler(
        host="192.168.129.133",
        username="cisco",
        password=getpass(),
        secret=getpass(),
        device_type="cisco_ios",
        session_log="my_session.txt")
net_connect.enable()
net_connect.find_prompt()
