


from requests import get
import os
import sys

email = sys.argv[1]


def discord():
  head = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; SM-J200BT Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36"}
  try:
    res = get(url = "https://discord.com:443/api/v6/experiments",headers=head)
    fingerprint = eval(res.text)["fingerprint"]
    cook = res.cookies.get_dict()
  except:
    return False

  try:
    payload = 'curl -q -s -X POST -d \'{"fingerprint":"%s","email":"%s","username":"Jorgin","password":"ajxnakxn","invite":null,"consent":true,"date_of_birth":"2001-02-08","gift_code_sku_id":null,"captcha_key":null}\' -H "User-Agent: Mozilla/5.0 (Linux; Android 5.1.1; SM-J200BT Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36" -H "Content-Type: application/json" -H "Referer: https://discord.com/register" -H "X-Fingerprint: %s" https://discord.com/api/v6/auth/register'%(fingerprint,email,fingerprint)
    out = os.popen(payload).read()
    print(out)
    if "Email is already registered." in out:
      print("FOUND!")
  except:
    return False

discord()
