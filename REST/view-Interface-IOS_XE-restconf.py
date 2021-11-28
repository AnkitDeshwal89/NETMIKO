import requests
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning
import json
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

#Set up connection parameters 
intf = input("Enter the Interface Name :")
router = {
        "ip":"192.168.129.139",
        "port":443,
        "user":"ankit",
        "password":"deshwal",
        "interf":intf
        }

#Set API header  By default we get XML , we will set to JSON

headers = {
        "Accept": "application/yang-data+json",
        "Content-Type":"application/yang-data+json"
        }

url = f"https://{router['ip']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface={router['interf']}"
response = requests.get(url,headers=headers,auth=(router['user'],router['password']),verify=False)

api_data =response.json()
pprint(api_data)
