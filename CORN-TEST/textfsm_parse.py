import textfsm
import subprocess
import random


res = subprocess.run('ifconfig',stdout=subprocess.PIPE)
intstatus = res.stdout.decode('ascii')
with open("datafile","w+") as a:
    a.write(intstatus)
    a.close()




template_file= "ifconfig-template.template"
template = open(template_file)


with open("datafile") as f:
    raw_data = f.read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_data)

print(data) 
NL = []
for x in data:
    NLD = {
            'Interface' : x[0].split(':')[0],
            'TX' : int(x[1])+int(random.randint(1,100))
         }
    NL.append(NLD)

print(NL)
import json
print('#'*12)
print(json.dumps(NL))

#Enter template FileName :ifconfig-template.template
#Input Data file : ifconfig_output.txt
