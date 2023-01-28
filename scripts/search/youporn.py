

from requests import post
import sys

email = sys.argv[1]

def youporn(email):
  try:
    head={"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
    res = post(url = f"https://www.youporn.com:443/users/check-unique/?email={email}",headers=head)
    if "true" in res.text:
      print("Found")
    else:
      return False
  except:
    return False

youporn(email)
