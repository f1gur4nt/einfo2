


from requests import get
import sys

email = sys.argv[1].replace("@","%40")

def pinterest():
  head={"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
  res = get(url = f"https://br.pinterest.com:443/resource/EmailExistsResource/get/?source_url=%2Fsignup%2Fstep1%2F&data=%7B%22options%22%3A%7B%22email%22%3A%22{email}%22%7D%2C%22context%22%3A%7B%7D%7D&_=1594799850336",headers=head)

  if '"data":true' in res.text:
    print("FOUND!")
  else:
    return False


pinterest()
