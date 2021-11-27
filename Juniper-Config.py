from jnpr.junos.utils.config import Config
from jnpr.junos import Device
from getpass import getpass


dev = Device(host="192.168.129.11",user="root",password=getpass())
dev.open()
dev.timeout = 60

cfg= Config(dev)

cfg.lock()

cfg.load("set system host-name JuniperMX-1",format="set",merge=True)

#cfg.rollback(0) to roll back

print(cfg.diff())

cfg.commit()

