

from requests import get,post
import sys
import re

email = sys.argv[1]

def armorgames(email):
  try:
    head={"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
    res = get(url="https://armorgames.com/register/email",headers=head)
    cook = res.cookies.get_dict()
    token = re.findall(r'name="_token" value="([\w]+)"',res.text)[0]

    dt = {"_token":token,"email":email}
    res2 = post(url="https://armorgames.com/register/check-email",headers=head,cookies=cook,data=dt)
    if "The email is not available" in res2.text:
      print("Found")
  except Exception as e:
    None

armorgames(email)
