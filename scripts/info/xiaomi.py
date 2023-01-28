
import requests
import sys
import re

email = sys.argv[1]

def xiaomi(email):
  try:
    print("\n====== Xiaomi Account Informations ======\n")
    head = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G"}
    session = requests.Session()
    res = session.get(url = f"https://account.xiaomi.com/pass/auth/resetPassword?user={email}&qs=callback%3Dhttps%253A%252F%252Faccount.xiaomi.com%252Fsts%253Fsign%253DZvAtJIzsDsFe60LdaPa76nNNP58%25253D%2526followup%253Dhttps%25253A%25252F%25252Faccount.xiaomi.com%25252Fpass%25252Fauth%25252Fsecurity%25252Fhome%2526sid%253Dpassport%26sid%3Dpassport",headers=head)

    html = res.text
    id = re.findall(r'var user="([\w]+)"',html)[0]
    print("User Id:",id)
  except Exception as e:
    print(e)

xiaomi(email)
