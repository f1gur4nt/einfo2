

from requests import get
import sys

email = sys.argv[1]

def fourshared(email):
  try:
    head = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; SM-J200BT Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36"}
    res = get(url = f"https://www.4shared.com:443/web/rest/usersWeb/validate?email={email}&coupon=", headers=head)
    if res.status_code == 403:
      print("Found")
    else:
      return False
  except:
    return False

fourshared(email)

