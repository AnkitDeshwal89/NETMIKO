from jinja2 import Template

filename = input("Enter Jinja2 File ending with .j2 : ")

with open(filename) as f:
    jinja_template_data = f.read()

myiplist = []
for ip in range(1,253):
    myiplist.append("10.1.1."+str(ip))
varforjinja = {
        'local_as':42,
        'router_id':"1.1.1.1",
        'peer1':myiplist,
        'remote_as':44
              }

j2_template = Template(jinja_template_data)
output = j2_template.render(**varforjinja)
print(output)
