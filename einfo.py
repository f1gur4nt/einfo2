

from requests import get,post
import argparse
import datetime
import glob
import sys
import os
import warnings


print("""

			███████╗██╗███╗   ██╗███████╗ ██████╗ 
			██╔════╝██║████╗  ██║██╔════╝██╔═══██╗
			█████╗  ██║██╔██╗ ██║█████╗  ██║   ██║
			██╔══╝  ██║██║╚██╗██║██╔══╝  ██║   ██║
			███████╗██║██║ ╚████║██║     ╚██████╔╝
			╚══════╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                      
						Coded by: https://github.com/f1gur4nt

""")


parser = argparse.ArgumentParser(description="Einfo - A Tool That Enumerate Emails Accounts, Get Informations and Bruteforce",epilog=f"Ex: python3 {sys.argv[0]} -e email@gmail.com")
parser.add_argument('-e',"--email", action = 'store', dest = 'email', help = 'Your Target Email')
parser.add_argument("-db","--db", action = 'store_true', dest = 'show_email_db', help = 'Show Wich Sites/Apps your Email Are Registred')
parser.add_argument("-l","--list", action = 'store_true', dest = 'list_edb', help = 'List Emails in Database')
arg = parser.parse_args()

def help():
  parser.print_help()
  exit()

def updater():
  my_version = open(".version.txt","r").read()
  current_version = get(url="https://raw.githubusercontent.com/f1gur4nt/einfo2/main/.version.txt").text
  if my_version != current_version:
    os.system("cd .. && rm -rf einfo2 && git clone https://github.com/f1gur4nt/einfo2")
    print("Has been updated successfully!! Please restart terminal!")
    exit()

def load_email_database():
  try:
    email_database = eval(open("db/email_database.json","r").read())
    return email_database
  except:
    print("[!] ERROR WHEN LOADING EMAIL DATABASE!")
    exit()

def email_database_save(database):
  try:
    edb = open("db/email_database.json","w+")
    edb.write(str(database))
    edb.close()
    print("[+] Saved in database!")
  except Exception as e:
    print(e)
    print("[!] Database save error!")

def show_registred_in_email():
  # VLW CURSO EM VIDEO!!!
  # https://m.youtube.com/watch?v=EGmlFdwD4C4
  try:
    email_db = load_email_database()
    edb = email_db[email]
    site_brute_scripts = glob.glob("scripts/bruter/*.py")
    print("")
    print("-"*56)
    print(f"[{'SITES/APPS':^16}] [{'DATA':^12}]  [{'BRUTEFORCE SCRIPT':^19}]")
    print("-"*56)

    for site_and_data in edb:
      site = site_and_data.split(" ")[0]
      if site in str(site_brute_scripts):
        bs = True
      else:
        bs = ""
      data = site_and_data.split(" ").pop()
      print(f"[{site:^16}] [{data:^12}]  [{str(bs):^19}]")
    print("-"*56)

    try:
      t = open(f"db/pwned_passwords/{email.replace('@','')}.txt")
      pwned = True
    except IOError:
      pwned = False

    print(f"\n[ Total: {len(edb)} ]")
    if pwned:
      print(f"\n[+] EMAIL ALREADY PWNED! SEE: db/pwned_passwords/{email.replace('@','')}.txt \n")

  except Exception as e:
    print(f"\n[!] {email} IS NOT INSIDE DATABASE :/")

def list_emails_in_database():
  try:
    edb = load_email_database()
    emails_sorted = []
    for e in edb:
      emails_sorted += [e]
    emails_sorted.sort()

    print("")
    print("-"*58)
    print(f"[{'EMAILS':^32}] [{'DATA':^12}] [{'PWNED':^6}]")
    print("-"*58)
    for e in emails_sorted:
      try:
        data = edb[e][0].split(" ").pop()
      except:
        data = "Unknown"
      try:
        t = open(f"db/pwned_passwords/{e.replace('@','')}.txt")
        pwned = True
      except IOError:
        pwned = ""

      print(f"[{e:^32}] [{data:^12}] [{str(pwned):^6}]")
    print("-"*58)
    print(f"\n[ Total: {len(edb)} ]\n")
  except Exception as e:
    print(e)

def account_search():
  total_sites = len(glob.glob("scripts/search/*.py"))
  site_search_scripts = glob.glob("scripts/search/*.py")
  email_database = load_email_database()
  try:
    my_edb = email_database[email]
  except:
    my_edb = []
  sites_found = []

  print(f"\n[*] SEARCHING FOR {email} in {total_sites} SITES/APPS ...\n")
  site_cont = 1
  for script in site_search_scripts:
    print(f"Status: {site_cont}/{total_sites}              \r",end="")
    site = script.split(".")[0].split("/").pop()
    if site in str(my_edb):
      print("[+] FOUND (db):",email,site.upper())
      site_cont += 1
      continue
    try:
      exists = bool(os.popen(f"timeout 20 python3 {script} {email}").read())
      if exists:
        print("[+] FOUND:",email,site.upper())
        data = datetime.date.today().strftime("%d/%m/%Y")
        if not site in str(my_edb):
          sites_found += [site+f" - {data}"]
      site_cont += 1
    except Exception as e:
      print(e)

  if sites_found != []:
    my_edb += sites_found
    email_database[email] = my_edb
    email_database_save(email_database)

def get_info():
  try:
    print("\n\n[*] GETING INFORMATIONS ABOUT SOME ACCOUNTS FOUND ...")
    site_info_scripts = os.popen("ls scripts/info/*.py").read().replace("scripts/info/","").split("\n")[:-1]
    edb = load_email_database()

    for sis in site_info_scripts:
      if sis.split(".")[0] in str(edb[email]):
        os.system(f"python3 scripts/info/{sis} {email}")
  except Exception as e:
    print(e)

def avaliable_bruters():
  print("\n[*] SEARCHING FOR AVALIABLES BRUTEFORCE SCRIPTS ...\n")
  edb = load_email_database()
  site_brute_scripts = os.popen("ls scripts/bruter/*.py").read().replace("scripts/bruter/","").split("\n")[:-1]

  for sbs in site_brute_scripts:
    if sbs.split(".")[0] in str(edb[email]):
      print(f"[+] AVALIABLE BRUTEFORCE SCRIPT TO {sbs.split('.')[0].upper()} ACCOUNTS!")
      print(f"See: scripts/bruter/{sbs}")

def google_search():
  os.system(f"python3 scripts/google_search.py {email}")

def check_pwned():
  os.system(f"python3 scripts/check_pwned.py {email}")

updater()

if arg.email != None:
  email = arg.email
  if arg.show_email_db:
    show_registred_in_email()
    exit()

elif arg.list_edb:
  list_emails_in_database()
  exit()
else:
  help()

account_search()
get_info()
#avaliable_bruters()
#check_pwned()
google_search()

