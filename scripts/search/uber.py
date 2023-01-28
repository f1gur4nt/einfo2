

from requests import post,get
import sys
import re

email = sys.argv[1]

def uber(email):
  try:
    head = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; SM-J200BT Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36"}
    true = True
    res = get(url = "https://auth.uber.com/login/session", headers=head)
    html = res.text
    head["x-csrf-token"] = re.findall(r"window.csrfToken = '([\w\-?]+)'",html)[0]
    cook = res.cookies.get_dict()

    dt = {"answer":{"type":"VERIFY_INPUT_EMAIL","userIdentifier":{"email":email}},"init":true}
    res = post(url = "https://auth.uber.com:443/login/handleanswer", headers=head,cookies=cook,json = dt)
    if res.status_code == 200:
      print("Found")
  except Exception as e:
    None

uber(email)
