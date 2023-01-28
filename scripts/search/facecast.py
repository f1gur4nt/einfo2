

from requests import post
import sys

email = sys.argv[1]

def facecast(email):
  try:
    head = {"User-Agent": "okhttp/3.14.9"}
    dt = {"email":email}
    res = post(url = "https://dhcxzil.facecast.xyz:443/faceshow/api/user/verification/exist/email",headers=head,data=dt)
    print(res.text)
    if '{"existUser":1}' in res.text:
      print("Found")
  except:
    None

facecast(email)
