from jnpr.junos.utils.config import Config
from jnpr.junos import Device
from getpass import getpass

dev = Device(host="192.168.129.11",user="root",password=getpass())
dev.open()
dev.timeout =60

cfg=Config(dev)
cfg.load(path="juniper_config.set",format="set",merge=True)

print(cfg.diff())

cfg.commit()
