

from requests import post
import sys
import re

email = sys.argv[1]

def pou(email):
  try:
    print("\n====== Pou Account Informations ======\n")
    head = {"User-Agent":"Apache-HttpClient/UNAVAILABLE (java 1.4)","Cookie": "unn_session=tLqw0a5wnTqbJyvawcsG333080786"}
    dt = {"a":""}
    res = post(url = f"http://app.pou.me:80/ajax/search/visit_user_by_email?e={email}&_a=1&_c=1&_v=4&_r=217",headers=head,data=dt)
    raw = res.text.replace("\\","").replace("\\","")
    nick = re.findall(r'"n":"([\w\£?\¢?\€?\¥?\^?\°?\=?\(?\)?\@?\#?\$?\%?\&?\-?\*?\:?\!?\™?\ ?\,?\/?\.?\√?\π?\÷?\×?\¶?\∆?]+)"',raw)[0]
    level = re.findall(r'"lvl":([\w]+)',raw)[0]
    fullness = re.findall(r'"fullness":([\w]+)',raw)[0] + "%"
    obesity = re.findall(r'"obesity":([\w]+)',raw)[0] + "%"
    energy = re.findall(r'"energy":([\w]+)',raw)[0] + "%"
    health = re.findall(r'"health":([\w]+)',raw)[0] + "%"
    fun = re.findall(r'"fun":([\w]+)',raw)[0] + "%"
    xp = re.findall(r'"xp":([\w]+)',raw)[0]
    dirty = str(bool(int(re.findall(r'"dirty":([\w]+)',raw)[0])))
    sleeping = str(bool(int(re.findall(r'"sleeping":([\w]+)',raw)[0])))
    print("Nickname:",nick)
    print("Level:",level)
    print("Food:",fullness)
    print("Obesity:",obesity)
    print("Energy:",energy)
    print("Health:",health)
    print("Fun:",fun)
    print("Xp:",xp)
    print("Dirty:",dirty)
    print("Sleeping:",sleeping)
  except Exception as e:
    print(e)

pou(email)
