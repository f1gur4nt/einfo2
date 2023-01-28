

from requests import post
import sys

email = sys.argv[1]

def betmines(email):
  try:
    head = {"User-Agent":"okhttp/3.12.0"}
    dt = {"username":email,"password":"sjjsmfkks29391ms"}
    res = post(url="https://api.betmines.com/betmines/v1/login",data=dt,headers=head)
    if res.status_code == 400:
      print("Found")
    else:
      return False
  except:
    None

betmines(email)
