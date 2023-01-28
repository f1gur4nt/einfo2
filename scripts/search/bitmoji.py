

from requests import post,delete
import sys
import re

email = sys.argv[1]

def bitmoji(email):
  global head
  global dt
  try:
    head = {"User-Agent":"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J200BT Build/LMY47X)"}
    head["bitmoji-user-agent"] = "1|com.bitstrips.imoji|11.6.0.6650|Android|5.1.1|samsung SM-J200BT|8ff008c6896e1771|1.5|pt_BR"
    dt = {"email":email,"password":"ksjcnsjd","appName":"bitmoji","birthday":"2004-03-16"}
    res = post(url = "https://bitmoji.api.snapchat.com/api/user",headers=head,json=dt)
    if res.status_code == 400:
      print("Found")
      return True
    elif "created" in res.text:
      return False
  except Exception as e:
    None

status = bitmoji(email)

if status == False:
  try:
    head = {"User-Agent":"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J200BT Build/LMY47X)"}
    dt = {"client_id":"imoji","client_secret":"ksjcnsjd","grant_type":"password","username":email,"password":"ksjcnsjd"}
    res = post(url = "https://bitmoji.api.snapchat.com/api/user/login",headers=head,data=dt)
    token = re.findall(r'"access_token":"([\w\-?]+)"',res.text)[0]
    head["bitmoji-token"] = token

    delete(url="https://bitmoji.api.snapchat.com/api/user",headers=head)
  except Exception as e:
    None
