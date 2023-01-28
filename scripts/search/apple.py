

from requests import post
import sys

exit()

email = sys.argv[1]

def apple():
  try:
    head = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; SM-J200BT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36"}
    head["Cookie"] = "idclient=web; dslang=BR-PT; site=BRA; aidsp=67C2D9BCA9969EEF332E289A217813F7D8618858F45F8C0C053854938AE9FCA587FEA677B028FBE684A4D2559AB53B2395FEFFCD87149E73156FA0DE6EF30FD00E204E52A95DD069BE10007147ECA02E8C0A8C11DBA6187822DAA773F53A12DD0BD70077AB0C7673D68A261A229E57B587F74B1C4C0BFC3A; geo=BR"
    head["X-Apple-ID-Session-Id"] = "67C2D9BCA9969EEF332E289A217813F7D8618858F45F8C0C053854938AE9FCA587FEA677B028FBE684A4D2559AB53B2395FEFFCD87149E73156FA0DE6EF30FD00E204E52A95DD069BE10007147ECA02E8C0A8C11DBA6187822DAA773F53A12DD0BD70077AB0C7673D68A261A229E57B587F74B1C4C0BFC3A"
    head["X-Apple-Request-Context"] = "create"
    head["X-Requested-With"] = "XMLHttpRequest"
    head["X-Apple-Api-Key"] = "cbf64fd6843ee630b463f358ea0b707b"
    dt = {"emailAddress":email}
    res = post(url = "https://appleid.apple.com/account/validation/appleid",headers=head,json=dt)
    print(res.status_code)
    print(res.text)
  except Exception as e:
    print(e)

apple()
