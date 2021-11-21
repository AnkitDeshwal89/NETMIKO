import yaml

my_data = {
        'username': 'alpha',
        'password': 'beta',
        'device': 'Cisco_gama',
        'ip_addr': '10.1.1.1',
        }
my_data['some_list'] = list(range(10))
my_data['null_value'] = None
my_data['bool'] = False


filename = input("Enter the FileName : ")
with open(filename,'wt') as f:
    yaml.dump(my_data,f,default_flow_style=False)  # default flow is False will generate yaml file from this data , while if True it will generate Json file from this data
