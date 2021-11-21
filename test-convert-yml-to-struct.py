import yaml
filename = input("Enter the FileName : ")
with open(filename) as f:
    yaml_out = yaml.safe_load(f)
print(yaml_out)
