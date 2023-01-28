

from requests import post
import sys

email = sys.argv[1]

def stoodi(email):
  try:
    head = {"User-Agent": "okhttp/3.12.1"}
    dt = {"email":email,"name":"","origin":"stoodi_android","password":"","phone":""}
    res = post(url = "https://www.stoodi.com.br/stoodiproginterface/v3/users/",headers=head,json=dt)
    if "Email already exists." in res.text:
      print("Found")
  except:
    None

stoodi(email)
