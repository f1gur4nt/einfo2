

from requests import get
import sys
import re

email = sys.argv[1]

def hentaistube(email):
  try:
    head={"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
    res = get(url=f"https://www.hentaistube.com/buscar-user?q={email}",headers=head)
    html = res.text
    if not "Nenhum resultado foi encontrado" in html:
      print("Found")
  except:
    None

hentaistube(email)
