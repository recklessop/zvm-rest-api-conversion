import requests
import json

# Define ZVM URL and credentials
zvm_url = "https://<zvm_ip_address>:9669/v1"
zvm_username = "<zvm_username>"
zvm_password = "<zvm_password>"

# Define headers for API requests
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Create session and authenticate with ZVM
session = requests.Session()
auth_data = {
    "AuthenticationMethod": "UserCredentials",
    "Username": zvm_username,
    "Password": zvm_password
}
auth_response = session.post(zvm_url + "/session/add", headers=headers, data=json.dumps(auth_data))
if auth_response.status_code != 200:
    print("Authentication failed with status code: {}".format(auth_response.status_code))
    exit()
else:
    print("Successfully authenticated with ZVM.")

# Get list of VPGs
vpg_response = session.get(zvm_url + "/vpgs", headers=headers)
if vpg_response.status_code != 200:
    print("Failed to retrieve VPGs with status code: {}".format(vpg_response.status_code))
    exit()

vpgs = json.loads(vpg_response.content)["Vpgs"]
print("Found {} VPGs:".format(len(vpgs)))
for vpg in vpgs:
    print("- {}".format(vpg["VpgName"]))

# Logout of session
session.delete(zvm_url + "/session", headers=headers)
print("Logged out of session.")
