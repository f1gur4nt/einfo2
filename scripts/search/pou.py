

from requests import post
import sys

email = sys.argv[1]

def pou(email):
  try:
    head = {"User-Agent": "Apache-HttpClient/UNAVAILABLE (java 1.4)"}
    res = post(url = f"http://app.pou.me/ajax/site/check_email?e={email}&_a=1&_c=1&_v=4&_r=217",headers=head)
    if "true" in res.text:
      print("Found")
    else:
      return False
  except:
    return False

pou(email)
