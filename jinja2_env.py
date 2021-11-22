from jinja2 import FileSystemLoader,StrictUndefined
from jinja2.environment import Environment 


# eve = Environment()                      This will ignore the paramerter missed while passing to jinja template
# eve.loader = FileSystemLoader('.')       This will load the file from current directory

eve = Environment(undefined=StrictUndefined) # this tell generate error for variable missed 
eve.loader = FileSystemLoader('./templates') # load the file from template directory

mylist = []
for x in range(1,253):
    mylist.append('10.1.1.'+str(x))

my_var = {
        'local_as': 42,
        'router_id': '1.1.1.1',
        'peer1':mylist,
        'remote_as': 45
        }

template_file = "bgp_config.j2"
template = eve.get_template(template_file)
output = template.render(**my_var)
print(output)

