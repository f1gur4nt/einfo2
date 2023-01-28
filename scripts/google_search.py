from requests import get
import sys
import re

email = sys.argv[1]

def google_search():
  global urls
  global urls_already

  head = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; nl) AppleWebKit/522.12.1 (KHTML, like Gecko) Version/3.0.1 Safari/522.12.2"}
  dork = f"intext:{email}"
  domain = re.findall(r"(@+[\w\.]+)",email)[0]
  try:
    res = get(url = f"https://www.google.com/search?q={dork}",headers=head,timeout=30)
    html = res.text
    raw_urls = re.findall(r'url\?q=([https?\://\w\.?\/?\_?\-?\&?\=?]+)',html)
    if "https://www.google.com/recaptcha/api.js" in html:
      print("[!] GOOGLE RECAPCHA HAVE BLOCKED YOU!")
      return
  except Exception as e:
    print("[!] GOOGLE SEARCH ERROR!")
    return

  urls = []
  urls_already = []

  def search_in_sites():
    global urls
    global urls_already
    print("\n[*] SEARCHING IN GOOGLE ...\n")
    for u in raw_urls:
      if not ".google.com" in u:
        if not u in urls:
          urls += [u.replace("&amp","")]

    if not urls:
      print(f"[!] NOTHING FOUND ABOUT {email} IN GOOGLE.")
      return

    for u in urls:
      if ".pdf" in u:
        if not u in urls_already:
          print("[-] SEE:",u)
          urls_already += [u]
          continue
      try:
        res = get(url = u,headers=head,timeout=30)
        html = res.text.lower()
        raw_emails = re.findall(rf'[\w\.?\-?\_?]+{domain}',html)
      except Exception as e:
        continue

      for e in raw_emails:
        if e == email:
          if not u in urls_already:
            print("[+] FOUND:",u)
            urls_already += [u]

  search_in_sites()

google_search()
