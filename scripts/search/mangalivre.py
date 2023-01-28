

from requests import get,post
import re
import sys

email = sys.argv[1]

def mangalivre(email):
  try:
    head = {"User-Agent":":Mozilla/5.0 (Linux; Android 5.1.1; SM-J200BT Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36"}
    dt = {"email":email}
    res = post(url="https://mangalivre.net/login/recover_password.json",headers=head,data=dt)
    if "success" in res.text:
      print("Found")
  except Exception as e:
    None

mangalivre(email)
