import json
from pprint import pprint


with open("inventory.json") as file:
    data = json.loads(file.read())

print("Python Object: " + str(type(data)))
print(data)
pprint(data)

i = 0

for item in data["response"]:
    print("Device ID: " + data["response"][i]["networkDeviceId"])
    i += 1
