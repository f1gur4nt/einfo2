

from requests import get,post
import re
import sys

email = sys.argv[1]


def redtube(email):
    head = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
    res = get(url = "https://www.redtube.com/register",headers=head)
    html = res.text
    token = re.findall(r'page_params.token = "([\w\_?\-?\.?]+.)"',html)[0]

    cook = res.cookies.get_dict()
    dt = {"token":token,"redirect":"","check_what":"email","email":email}
    head = {"X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","Referer":"https://www.redtube.com/register",'language':'{"lang":"en","showMsg":false}'}
    res = post(url = "https://www.redtube.com:443/user/create_account_check?token={}".format(token),cookies=cook,headers=head,data=dt)

    if "Email has been taken" in res.text:
      print("True")

    else:
      return

try:
  redtube(email)
except:
  None
