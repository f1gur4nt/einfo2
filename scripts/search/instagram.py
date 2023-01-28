

from requests import get,post
import sys
import re

email = sys.argv[1]

def instagram(email):
  try:
    head = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","Accept-Encoding":"gzip, deflate","Accept-Language":"en-US"}
    res1 = get(url="https://www.instagram.com/accounts/emailsignup/",headers=head)
    html1 = res1.text
    csrf_token = re.findall(r'\\"csrf_token\\":\\"([\w\-?\_?\.?]+)\\"',html1)[0]
    cook = res1.cookies.get_dict()

    head["X-CSRFToken"] = csrf_token
    head["X-Instagram-AJAX"] = "1006715685"
    head["X-IG-App-ID"] = "936619743392459"
    head["X-ASBD-ID"] = "198387"
    head["X-IG-WWW-Claim"] = "0"
    head["X-Requested-With"] = "XMLHttpRequest"
    head["Referer"] = "https://www.instagram.com/accounts/emailsignup/"
    
    dt = {'email':email,'username':'','first_name':'','opt_into_one_tap':'false'}
    res2 = post(url="https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/",headers=head,cookies=cook,data=dt)
    html2 = res2.text
    if "using the same email" in html2:
      print("Found")
  except Exception as e:
    print(e)

instagram(email)
