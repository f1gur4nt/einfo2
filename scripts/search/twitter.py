

import requests
import sys
import re


email = sys.argv[1]

def twitter(email):
  try:
    head = {"User-Agent":":Mozilla/5.0 (Linux; Android 5.1.1; SM-J200BT Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36"}
    session = requests.Session()
    res = session.get(url="https://twitter.com/account/begin_password_reset",headers=head)
    token = re.findall(r'name="authenticity_token" value="([\w]+)"',res.text)[0]
    dt = {"authenticity_token":token,"account_identifier":email}
    res = session.post(url="https://twitter.com/account/begin_password_reset",headers=head,data=dt)
    if res.url == "https://twitter.com/account/verify_user_info":
      print("Found")
  except:
    None

twitter(email)
