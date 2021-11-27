from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from getpass import getpass
from pprint import pprint
import ipdb


dev = Device(host = "192.168.129.11", user="root" , password = getpass())
dev.open()

ports = EthPortTable(dev)
ports.get()

#ipdb.set_trace()
print('*'*12)
pprint(ports)
print('*'*12)
pprint(ports.keys())
print('*'*12)
pprint(ports.values())
print('*'*12)
pprint(ports.items())
print("#"*12)
