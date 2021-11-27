from jnpr.junos import Device
from getpass import getpass
from pprint import pprint
from jnpr.junos.op.arp import ArpTable

dev = Device(host="192.168.129.11",user="root",password=getpass())
dev.open()

arp_entry = ArpTable(dev)
arp_entry.get()

pprint(arp_entry)
