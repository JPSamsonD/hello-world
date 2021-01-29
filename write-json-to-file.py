# Import the requests library to make REST calls
import requests
# Import JSON library for formatting login requests to DNA Center
import json

# Disable certificate warning
requests.packages.urllib3.disable_warnings()

# Body of data consisting of username and password to get a cookie from APIC
encoded_body = json.dumps({
	"aaaUser": {
		"attributes": {
			"username":"devnetuser",
			"password":"Cisco123!"
		}
	}
})

# REST calls will use the URL for the DNA Center as the base URL
# Define a variable the DNAC IP or DNS
dnac_url = "https://sandboxdnac.cisco.com"

# Username and Password to access DNAC
# credential = {"username":"devnetuser", "password":"Cisco123!"}

token_url = dnac_url + "/api/system/v1/auth/token"

# Content type must be specified in the header
header = {"content-type":"application/json"}

# Perform a POST to DNAC to get the token
resp = requests.post(token_url, data=encoded_body, headers=header, verify=False)

# Convert response to JSON format
resp_json = resp.json()

# Parse the JSON data to get the token
token = resp_json["Token"]

# List 3 of the devices in the network
get_devices_url = dnac_url + '/api/v1/network-device/1/3'

# Include content type and ticket in the header
header = {"content-type":"application/json", "X-Auth-Token":token}

# Perform GET on get_devices_url
get_devices_response = requests.get(get_devices_url, headers=header, verify=False)

# Response comes in JSON format
get_devices_json = get_devices_response.json()

# Display information from the JSON data received
parent = get_devices_json["response"]

print("Devices = ")

with open("Device_List_1.txt", "w") as file:
    for item in parent:
        device = "id = " + item["id"] + " type = " + item["type"]
        file.write(device + "\n")
        print(device)
