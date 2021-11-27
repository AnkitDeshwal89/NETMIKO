from getpass import getpass
from pprint import pprint
from napalm import get_network_driver
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
Cisco = {
        "hostname":"192.168.129.133",
        "device_type":"ios",
        "username":"cisco",
        "password":getpass(),
        "optional_args":{},

        }

Juniper = {
        "hostname":"192.168.129.11",
        "device_type":"junos",
        "username":"root",
        "password":getpass(),
        "optional_args":{},
        }

Nxos = {
        "hostname":"192.168.129.135",
        "device_type":"nxos",
        "username":"admin",
        "password":getpass(),
        "optional_args":{},
       }





device_Cisco = Cisco.pop("device_type")
driver_Cisco = get_network_driver(device_Cisco)
device_c  = driver_Cisco(**Cisco)

device_c.open()

device_Juniper = Juniper.pop("device_type")
driver_Juniper = get_network_driver(device_Juniper)
device_j  = driver_Juniper(**Juniper)

device_j.open()

device_nxos = Nxos.pop("device_type")
driver_nxos = get_network_driver(device_nxos)
device_nx  = driver_nxos(**Nxos)
device_nx.open()


print("*"*48)
pprint(device_c.get_facts())
print("*"*48)
pprint(device_j.get_facts())
print("*"*48)
pprint(device_nx.get_facts())
