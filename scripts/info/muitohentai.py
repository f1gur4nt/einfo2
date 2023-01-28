

from requests import get
import sys
import re

email = sys.argv[1]

def muitohentai(email):
  print("\n====== Muito Hentai Account Informations ======\n")
  head={"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
  try:
    res = get(url=f"https://www.muitohentai.com/buscar-user/?q={email}",headers=head)
    html = res.text
    if not "Nenhum resultado foi encontrado" in html:
      profile_name = re.findall(r'<a href="/user/([\w\.?\ ?\@?\#?\%?\&?\-?\+?\_?\!?\??\'?\"?\:?\(?\)?]+)/',html)[0]
      print("Profile Name:",profile_name)
      print("Profile Url:",f"https://www.muitohentai.com/user/{profile_name}/")
  except:
    None

muitohentai(email)

