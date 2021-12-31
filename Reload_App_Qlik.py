
import requests

requests.packages.urllib3.disable_warnings()

# Header
xrf = 'iX83QmNlvu87yzAB'
headers = {'X-Qlik-xrfkey': xrf,
           "Content-Type": "application/json",
           "X-Qlik-User":"UserDirectory=hospinet;UserId=felix.kraemer"}

cert = '//db-rb-fs001/data_qlik_desktop/data_source_apps/_scripts/ExternalTaskTrigger/clientandkey.pem'

id= 'cb2f07b3-8570-4970-ab15-8f8b083bbf89'

url = f"https://dwa-hq-ql001.hospinet.net:4242/qrs/reloadtask/{id}?xrfkey={xrf}"

resp = requests.post(url, headers=headers, verify=False, cert=cert)
print(resp.status_code)
print(resp.json())

obj = resp.json()

for part in obj:
    print(part)
