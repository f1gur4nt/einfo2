


from requests import get
import sys

email = sys.argv[1]

def spotify():
  head={"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
  res = get(url = f"https://spclient.wg.spotify.com:443/signup/public/v1/account?validate=1&email={email}",headers=head)
  if '"status":20' in res.text:
    print("FOUND")
  else:
    return False

try:
  spotify()
except:
  None
