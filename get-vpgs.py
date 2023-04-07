import requests
from requests.structures import CaseInsensitiveDict

strZVMIP = "ZVM IP"
strZVMPort = "ZVM HTTPS port"
strZVMUser = "ZVM user"
strZVMPwd = "ZVM user password"

def getxZertoSession(userName, password):
    baseURL = f"https://{strZVMIP}:{strZVMPort}"
    xZertoSessionURL = f"{baseURL}/v1/session/add"
    authInfo = f"{userName}:{password}".encode('utf-8')
    authInfo = base64.b64encode(authInfo).decode('utf-8')
    headers = CaseInsensitiveDict()
    headers["Authorization"] = f"Basic {authInfo}"
    contentType = "application/json"
    response = requests.post(xZertoSessionURL, headers=headers, json={}, verify=False)
    return response.headers.get("x-zerto-session")

#Extract x-zerto-session from the response, and add it to the actual API:
xZertoSession = getxZertoSession(strZVMUser, strZVMPwd)
zertoSessionHeader = {"x-zerto-session": xZertoSession}

# Get list of VPGs
baseURL = f"https://{strZVMIP}:{strZVMPort}"
ZertoURL = f"{baseURL}/v1/vpgs"
vpg_response = session.get(ZertoURL, headers=zertoSessionHeader, verify=False)

if vpg_response.status_code != 200:
    print("Failed to retrieve VPGs with status code: {}".format(vpg_response.status_code))
    exit()

vpgs = json.loads(vpg_response.content)
for vpg in vpgs:
    print(vpg)

# Logout of session
session.delete(zvm_url + "/session", headers=headers)
print("Logged out of session.")
