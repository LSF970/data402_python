import json

# json.load() --> Takes a file and converts to a dict
path_to_json = "example.json"
with open(path_to_json) as jsonfile:
    json_data = json.load(jsonfile)
value = json_data["ip"]

print(value)

# with open("new_json_file.json") as jsonfile:
#     car = json.load(jsonfile)
#     print(type(car))
#     print(car["name"])
#     print(car["engine"])

# json.loads() --> Takes a string and converts to a dict
path_to_json = "example.json"
with open(path_to_json) as jsonfile:
    json_data = json.loads(jsonfile.read())
value = json_data["ip"]

print(value)