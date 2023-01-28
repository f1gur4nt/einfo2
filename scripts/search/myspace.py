

from requests import post
import sys

email = sys.argv[1]

def myspace(email):
  try:
    head = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G","X-Requested-With": "XMLHttpRequest","Referer": "https://myspace.com/signup/email"}
    hash = "MTMzM2Y0OThmZTJjMGEyYsKqw5DCoA3DklNIw77CscOSCmdmw61cw4pkw4ZGw6sfw7/CqTQ8csKHBMOSw4bCjcOSPGTDmyR9LcO0GzHDnMORAygxOcO7wo0Ew6zCkMOhw5vCtTt7wqfDh1tcJ8KPBXTCu8KWw7NywrvCrcOewpwZwq/DnMKEB3TCv3dqSsOrw7jCswXDtsOkwqnCrlpGwr3CrGDDrntbw7/ClsOKbsKwa8KMwq3Dr1hrSsOb"
    head["Hash"] = hash
    dt = {"email":email}
    res = post(url = "https://myspace.com:443/ajax/account/validateemail",timeout=5,headers=head,data=dt)
    html = res.text
    if "FailedDuplicateEmail" in html:
      print("Found")
    else:
      return False
  except:
    None

myspace(email)
