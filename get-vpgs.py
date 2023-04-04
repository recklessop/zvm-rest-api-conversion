import requests
import json

# ZVM connection details
zvm_url = "https://192.168.50.60"
zvm_username = "admin"
zvm_password = "Zertodata987!"

# Zerto REST API endpoint URLs
vpgs_url = zvm_url + "/v1/vpgs"

# Set headers for Zerto REST API requests
headers = {
    "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Get Keycloak access token
token_url = zvm_url + "/auth/realms/zerto/protocol/openid-connect/token"
token_data = {
    "grant_type": "password",
    "username": zvm_username,
    "password": zvm_password,
    "client_id": "zerto-client",
    "scope": "email profile"
}
token_response = requests.post(token_url, headers=headers, data=token_data, verify=False)
if token_response.status_code != 200:
    print(token_response.content)
    print("Failed to retrieve Keycloak access token with status code: {}".format(token_response.status_code))
    exit()

#extract the access token from the response
access_token = json.loads(token_response.content)["access_token"]

#setup headers for Zerto REST API requests using the access token
headers["Authorization"] = "Bearer " + access_token

# Get list of VPGs using the access token in the header
vpgs_response = requests.get(vpgs_url, headers=headers, verify=False)
if vpgs_response.status_code != 200:
    print("Failed to retrieve VPGs with status code: {}".format(vpgs_response.status_code))
    exit()

vpgs_data = json.loads(vpgs_response.content)
for vpg in vpgs_data:
    print(vpg)
