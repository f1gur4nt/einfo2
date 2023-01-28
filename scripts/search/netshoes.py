

from requests import get
import sys

email = sys.argv[1]

def netshoes(email):
  try:
    head={"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
    res = get(url="https://www.netshoes.com.br/v2/auth/account/exists/"+email,headers=head)
    if "true" in res.text:
      print("Found")
  except Exception as e:
    None

netshoes(email)
