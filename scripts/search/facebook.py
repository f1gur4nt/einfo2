

from requests import get,post
import sys
import re

email = sys.argv[1]

def facebook(email):
  head={"Host":"m.facebook.com","Connection":"keep-alive","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","Accept-Encoding":"gzip, deflate","Accept-Language":"en-US"}
  try:
    resposta1=get(url="https://m.facebook.com/login/identify/?ctx=recover&search_attempts=0&ars=facebook_login&alternate_search=0&toggle_search_mode=1",headers=head)
    cook = resposta1.cookies.get_dict()
    lsd = re.findall('type="hidden" name="lsd" value="([\w]+)"',resposta1.text)[0]
    jazoest = re.findall(r'input type="hidden" name="jazoest" value="([\w]+)"',resposta1.text)[0]
    dt={"lsd":lsd,"jazoest":jazoest,"email":email,"did_submit":"Search"}
    head={"Host":"m.facebook.com","Connection":"keep-alive","Content-Length":"89","Cache-Control":"max-age=0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Origin":"https://m.facebook.com","User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","Content-Type":"application/x-www-form-urlencoded","Referer":"https://m.facebook.com/login/identify/?ctx=recover&search_attempts=0&ars=facebook_login&alternate_search=0&toggle_search_mode=1","Accept-Encoding":"gzip, deflate","Accept-Language":"en-US"}
    resposta2=post(url="https://m.facebook.com/login/identify/?ctx=recover&search_attempts=1&ars=facebook_login&alternate_search=1",data=dt,headers=head,cookies=cook)
  except Exception as e:
    return False

  if "https://m.facebook.com/login/identify/?ctx=recover&search_attempts" in resposta2.url:
    return False
  else:
    print(str(email)+" FACEBOOK (True)")

facebook(email)
