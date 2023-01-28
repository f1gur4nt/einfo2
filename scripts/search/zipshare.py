

from requests import post
import sys

email = sys.argv[1]

def zipshare(email):
  try:
    head = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; SM-J200BT Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36"}
    res = post(url = "https://www.zipshare.com:443/userprofile/check",data={"email":email},headers=head)
    if "true" in res.text:
      print("Found")
    else:
      return False
  except:
    None

zipshare(email)
