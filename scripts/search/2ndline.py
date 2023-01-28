

from requests import head
import sys

email = sys.argv[1]

def ndline(email):
  try:
    h = {"User-Agent":"TextNow 6.9.0.1 (SM-J200BT; Android OS 5.1.1; pt_BR)"}
    res = head(url = f"https://api.2ndline.me:443/api2.0/emails/{email}?client_type=2L_ANDROID",headers=h)
    if res.status_code == 200:
      print("Found")
  except Exception as e:
    None

ndline(email)
