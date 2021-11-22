import textfsm

template_file= input("Enter template FileName :")
template = open(template_file)

datafile=input("Input Data file : ")

with open(datafile) as f:
    raw_data = f.read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_data)

print(data)
NL = []
for x in data:
    NLD = {
            'Interface' : x[0].split(':')[0],
            'IP' : x[1]
         }
    NL.append(NLD)

print(NL)
import json
print('#'*12)
print(json.dumps(NL))

#Enter template FileName :ifconfig-template.template
#Input Data file : ifconfig_output.txt
