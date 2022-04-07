import requests
import json
def get_tele_msg():
    a=requests.get('https://api.telegram.org/bot5032770954:AAEq_ekucF6PG7aOMpF-cSrr_yj_rf1C-Bc/getUpdates').text
    a=json.loads(a)
    b=len(a["result"])-1
    message=a["result"][b]["message"]["text"]
    name=a["result"][b]["message"]["chat"]["username"]
    return (message,name)
message,name=get_tele_msg()
b=open("ganesh.py","w")
c=message
b.write(c)
b.close()
print(message)
import ganesh