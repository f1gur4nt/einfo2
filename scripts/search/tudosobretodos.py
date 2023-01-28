

from requests import post
import sys

# DISABLED, BUT WORKS
exit()

email = sys.argv[1]

def tudosobretodos(email):
  try:
    head = {"User-Agent":"Mozilla/5.0 (Linux; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36"}
    dt = {"usuario":email}
    res = post(url="https://tudosobretodos.info/checarUsuario",headers=head,data=dt)
    if '"existente":"1"' in res.text:
      print("Found")
  except:
    None

tudosobretodos(email)
