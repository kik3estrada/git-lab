"""
Module to connect to Apic and query  the Tenant MOs
"""
import requests
import json
requests.packages.urllib3.disable_warnings()
encoded_body = json.dumps({
"aaaUser": {
"attributes": {
"name": "admin",
"pwd": "ins4956!"
}
}
})
resp = requests.post("https://10.31.127.17/api/aaaLogin.json", data=encoded_body, verify=False)
header = {"Cookie": "APIC-cookie=" + resp.cookies["APIC-cookie"]}
tenants = requests.get("https://10.31.127.17/api/node/class/fvTenant.json?rsp-subtree-include=health,faults", headers=header, verify=False)
mytenants=json.loads(tenants.text)
print(mytenants)
