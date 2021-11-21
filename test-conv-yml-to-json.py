import json

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
    json.dump(my_data,f, indent=4)  

print('#'*12)
print(my_data)
print('#'*12)
print()
print('*'*12)
print(json.dumps(my_data))  # json.dumps is used to display on screen where as json.dump is used to writye in file 
print('*'*12)
