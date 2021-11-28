import requests
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning
import json
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

#Set up connection parameters 

router = {
        "ip":"192.168.129.139",
        "port":443,
        "user":"ankit",
        "password":"deshwal",
        }

#Set API header  By default we get XML , we will set to JSON

headers = {
        "Accept": "application/yang-data+json",
        "Content-Type":"application/yang-data+json"
        }

body = json.dumps({
        "ietf-interfaces:interface": {
            "name":"Loopback100",
            "description":"Added BY python restconf-cli",
            "type":"iana-if-type:softwareLoopback",
            "enabled":True,
            "ietf-ip:ipv4": {
                  "address" : [
                      {
                        "ip":"192.168.122.1",
                        "netmask":"255.255.255.0"
                          }
                       ]
                }

            }
       })


url = f"https://{router['ip']}/restconf/data/ietf-interfaces:interfaces"

response = requests.request("POST",url,headers=headers,data=body,auth=(router['user'],router['password']),verify=False)

print(response.text)
