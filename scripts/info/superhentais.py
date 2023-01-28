

from requests import get
import sys
import re

email = sys.argv[1]

def superhentais(email):
  print("\n====== Super Hentais Account Informations ======\n")
  head={"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
  try:
    res = get(url = f"https://www.superhentais.com/perfil/busca?search_user={email}",headers=head)
    html = res.text
    if "rio encontrado!" in html:
      try:
        profile_url = re.findall(r'<h3><a href="(https://www.superhentais.com/perfil/[\w]+)" title="Perfil ',html)[0]
        name = re.findall(r'<h3><a href="https://www.superhentais.com/perfil/[\w]+" title="Perfil ([\w\ ?\@?\#?\$?\%?\&?\-?\+?\(?\)?\,?\™?\??\!?\,?\/?]+)',html)[0]
      except:
        None
      print("Name:",name)
      print("Profile Url:",profile_url)
  except:
    None

superhentais(email)
