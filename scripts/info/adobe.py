

from requests import get,post
import sys

email = sys.argv[1]

def adobe(email):
  try:
    print("\n====== Adobe Account Informations ======\n")
    head = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; SM-J200BT Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36","x-ims-clientid":"adobedotcom2"}
    res = get(url = "https://auth.services.adobe.com/en_US/index.html?callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fadobeid%2Fadobedotcom2%2FAdobeID%2Ftoken%3Fredirect_uri%3Dhttps%253A%252F%252Fwww.adobe.com%252F%2523from_ims%253Dtrue%2526old_hash%253D%2526api%253Dauthorize%26state%3D%257B%2522ac%2522%253A%2522%2522%257D%26code_challenge_method%3Dplain%26use_ms_for_expiry%3Dtrue&client_id=adobedotcom2&scope=creative_cloud%2CAdobeID%2Copenid%2Cgnav%2Cread_organizations%2Cadditional_info.projectedProductContext%2Csao.ACOM_CLOUD_STORAGE%2Csao.stock%2Csao.cce_private%2Cadditional_info.roles&denied_callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fdenied%2Fadobedotcom2%3Fredirect_uri%3Dhttps%253A%252F%252Fwww.adobe.com%252F%2523from_ims%253Dtrue%2526old_hash%253D%2526api%253Dauthorize%26response_type%3Dtoken%26state%3D%257B%2522ac%2522%253A%2522%2522%257D&state=%7B%22ac%22%3A%22%22%7D&relay=498c7318-8bca-4218-b5e7-fd96f8a6328d&locale=en_US&flow_type=token&idp_flow_type=login#/signup",headers=head)
    cook = res.cookies.get_dict()
    head["Content-Type"] = "application/json;charset=UTF-8"
    head["Accept-Language"] = "en-US;q=0.8"
    dt = {"username":email}
    res = post(url = "https://auth.services.adobe.com/signin/v2/users/accounts",headers=head,json=dt)
    true = True
    false = False
    null = None
    json = eval(res.text)
    j = json[0]
    print("Type:",j["type"])
    print("Status:",j["status"]["code"])
    print("images:",j["images"])
    print("hasT2ELinked:",j['hasT2ELinked'])
  except Exception as e:
    None

adobe(email)
