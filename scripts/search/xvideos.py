

import sys
from requests import get

email = sys.argv[1]


def xvideos(email):
    global xvideos

    email = email.replace("@","%40")
    head = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
    res = get(url = "https://www.xvideos.com:443/account/checkemail?email={}".format(email),headers=head)

    if "false" in res.text:
      print("Found")

    else:
      return


try:
  xvideos(email)
except:
  None
