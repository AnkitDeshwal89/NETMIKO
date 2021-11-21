import json
filename = input("Enter the FileName : ")
with open(filename) as f:
    json_out = json.load(f)
print(json_out)
