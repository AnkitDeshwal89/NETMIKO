import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
from getpass import getpass
from nxapi_plumbing import Device
from lxml import etree
import string
requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #to disable ssl inscure warning

device = Device (
        api_format = "xml",
        host = "192.168.129.135",
        username = "admin",
        password = getpass(),
        transport="https",
        port= 443,
        verify = False,
        )

output = device.show("show hostname")
print(output)
print("#"*12)
print(etree.tostring(output).decode())
