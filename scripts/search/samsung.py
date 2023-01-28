

from requests import get,post
import sys
import re

email = sys.argv[1]

def samsung(email):
  try:
    head = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; SM-J200BT Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36"}
    res = get(url="https://account.samsung.com/accounts/v1/MBR/signUp",headers=head)
    html = res.text
    head["X-CSRF-TOKEN"] = re.findall(r"{'token': '([\w\-?]+)'",html)[0]
    cook = res.cookies.get_dict()

    dt = {"emailID":email}
    res2 = post(url="https://account.samsung.com/accounts/v1/MBR/signUpCheckEmailIDProc",headers=head,cookies=cook,json=dt)
    if "Account already exists." in res2.text:
      print("Found")
  except Exception as e:
    print(e)

samsung(email)
