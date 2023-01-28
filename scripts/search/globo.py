

from requests import get
import sys

email = sys.argv[1]

def globo(email):
  head={"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
  try:
    res = get(url = f"https://login.globo.com:443/api/v1/usuarios/{email}",headers=head)
    if res.status_code == 200:
      print("Found")
    else:
      return False
  except:
    return False

globo(email)
