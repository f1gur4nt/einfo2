

from requests import post
import sys

email = sys.argv[1]

def anime_planet(email):
  try:
    head={"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","accept-language":"en-US"}
    dt = {"username":"088c6ebba74cf7c37a35ae8de048e584","email":email,"password1":"akkdmwkdk@1991","month":"4","day":"1","year":"2001","capt-auth":"WwJGJxAheA7Tg2U","g-recaptcha-response":"","recaptcha":"5f4b3433d318577a313f05ed5b252aacb47821e211f9128a30c76ac93c2b36fd3f860c78","signup":"1","page":""}
    res = post(url = "https://www.anime-planet.com/sign-up",data=dt,headers=head)
    if "This email address is already taken" in res.text:
      print("Found")
    else:
      return False
  except:
    return False

anime_planet(email)
