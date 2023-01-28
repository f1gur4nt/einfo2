

# https://api.picsart.com:443/search/home/artist/results?q=zuelbilah2%40protonmail.com

from requests import get
import sys

email = sys.argv[1]

def picsart(email):
  head = {"User-Agent":"PicsArt-10.x"}
  true = 1
  false = 0
  null = None
  print("\n====== Pics Art Account Informations ======\n")
  try:
    res = get(url = f"https://api.picsart.com:443/search/home/artist/results?q={email}",headers=head)
    son = eval(res.text)
    if son["response"][0]["data"][0]["name"] == email or son["response"][0]["data"][0]["username"] == email or son["response"][0]["data"][0]["username"] == email.split("@")[0]:
      if son["response"][0]["data"][0]["username"] == email.split("@")[0]:
        print("WARNING: Can be a false positive!\n")
      print("Id:",son["response"][0]["data"][0]["id"])
      print("User:",son["response"][0]["data"][0]["name"])
      print("Username:",son["response"][0]["data"][0]["username"])
      print("Photo:",son["response"][0]["data"][0]["photo"])
      print("Followers:",son["response"][0]["data"][0]["followers_count"])
      print("Following:",son["response"][0]["data"][0]["following_count"])
  except Exception as e:
   None

picsart(email)
