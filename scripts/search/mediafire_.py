

from mediafire import MediaFireApi
from requests import post
import sys

email = sys.argv[1]

def create_account_method():
  try:
    head = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","Accept-Encoding":"gzip, deflate","Accept-Language":"en-US"}
    dt = {'response_format':'json','email':email,'password':'figurante123cuzin1','application_id':'35','first_name':'','last_name':''}
    res = post(url = "https://www.mediafire.com/api/1.5/user/register.php",headers=head,data=dt)
    html = res.text
    if "The email address you specified is found to be rejected" in html:
      return True
    elif "The email address you specified is already in use" in html:
      return True
  except Exception as e:
    None

def login_method():
  try:
    api = MediaFireApi()
    session = api.user_get_session_token(email=email,password="figurante123cuzin1",app_id="42511")
    return True
  except Exception as e:
    None

found = create_account_method()
if found:
  logged = login_method()
  if not logged:
    print("Found")

