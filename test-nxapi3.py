import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
from getpass import getpass
from nxapi_plumbing import Device

requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #to disable ssl inscure warning

device = Device (
        api_format = "jsonrpc",
        host = "192.168.129.135",
        username = "admin",
        password = getpass(),
        transport="https",
        port= 443,
        verify = False,
        )

cfg_cmd = [
        "logging history size 300"
      ]
output = device.config_list(cfg_cmd)
print(output)
