

from requests import get
import sys

email = sys.argv[1]

def picsart(email):
  head = {"User-Agent":"PicsArt-10.x"}
  try:
    res = get(url = f"https://api.picsart.com:443/users/email/existence?emails={email}",headers=head)
    if email in res.text:
      print("Found")
    else:
      return False
  except:
    return False

picsart(email)
