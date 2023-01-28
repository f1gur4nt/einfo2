

import os

# bruninha@gmail.com
#bruna = ['2ndline', '4shared','adobe', 'discord', 'instagram', 'picsart', 'pinterest', 'pornhub', 'pou', 'redtube', 'samsung', 'spotify', 'stoodi', 'twitter', 'xvideos']
joao = ['2ndline', 'pornhub', 'hentaistube', 'redtube', 'discord', 'twitter', 'muitohentai', 'armorgames', 'instagram', 'mediafire_', 'betmines', 'mangalivre', 'bitmoji', 'pou', 'youporn', '4shared', 'samsung', 'xvideos', 'facecast', 'pinterest', 'myspace', 'adobe', 'spotify', 'stoodi', 'netshoes', 'globo', 'picsart', 'facebook']
zuelbilah2 = ['4shared', 'anime-planet', 'bitmoji', 'discord', 'facecast', 'globo', 'hentaistube', 'instagram', 'mangalivre', 'mediafire_', 'muitohentai', 'myspace', 'picsart', 'pinterest', 'pornhub', 'pou', 'spotify', 'stoodi', 'uber', 'xvideos','zipshare']

def remove_duplicated(lista):
  for site in lista:
    if site in joao:
      lista.remove(site)

remove_duplicated(zuelbilah2)
#remove_duplicated(joao)

total_sites = set(joao + zuelbilah2)
found = []
tested = []

print(total_sites)

def verify(email,sites_list):
  global found
  global tested
  global scripts
  scripts = os.popen("ls *.py").read().split("\n")[:-1]
  for script in scripts:
    try:
      if not script.split(".")[0] in sites_list:
        continue
      elif script.split(".")[0] in tested:
        continue
      print(f"Checking if {script} works ... ")
      out = os.popen(f"python3 {script} {email}").read()
      if out:
        found += [script.split(".")[0]]
        tested += [script.split(".")[0]]
    except Exception as e:
      print(e)


print("\n[*] VERIFYING IF SCRIPTS ARE WORKING (False-Negative Method)")
verify("joao@gmail.com",joao)
verify("zuelbilah2@protonmail.com",zuelbilah2)

out=os.popen("rm NOT_WORKING.TXT").read()
not_working = open("NOT_WORKING.TXT","a")
not_working_txt = open("NOT_WORKING.TXT","r").read()

print("[-] RESULT:\n")
not_cont = 0
for s in total_sites:
  if not s in found:
    print(f"\33[41m [WARNING] {s} Are Not Working :/\33[0m")
    not_cont += 1
    if not s in not_working_txt:
      not_working.write(s+"\n")

print(f"\n[*] Total Not Working: {not_cont}/{len(scripts)}")
print(f"[*] Total Tested: {len(total_sites)}")
print(f"[*] Total Not Tested:",len(scripts)-len(total_sites))
print("[*] Scripts not tested:")
scripts = os.popen("ls *.py").read().split("\n")[:-1]

for s in scripts:
  if not s.split(".py")[0] in total_sites:
    print(s)


not_working.close()
