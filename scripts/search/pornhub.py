
from requests import get,post
import sys
import re

email = sys.argv[1]

def pornhub(email):
    global pornhub
    head = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
    res = get(url = "https://www.pornhub.com/signup",headers=head)
    html = res.text
    token=re.findall(r'data-autocomplete="token=([\w\.?\-?\_?]+)&',html)[0]

    cook = res.cookies.get_dict()
    dt = {"token":token,"captcha_type":"v3","check_what":"email","taste_profile":"","email":email,"username":"","password":""}
    head = {"Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","Referer":"https://www.pornhub.com/signup",}
    res = post(url = "https://www.pornhub.com:443/user/create_account_check?token={}".format(token),data=dt,headers=head,cookies=cook)
    html = res.text

    if "Email has been taken" in html:
      print("True")
    else:
      return

try:
  pornhub(email)
except:
  None
