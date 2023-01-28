

from requests import post
import sys

email = sys.argv[1]

def procuroacho(email):
  try:
    head = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","Accept-Encoding":"gzip, deflate","Accept-Language":"en-US"}
    dt = {"email":email}
    res = post(url="https://www.procuroacho.com/new-account-email-check",headers=head,data=dt)
    if "true" in res.text:
      print("found")
  except Exception as e:
    print(e)

procuroacho(email)

