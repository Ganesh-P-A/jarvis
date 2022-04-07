import urllib.request
import time
import webbrowser
import requests
import json

def send(message):
    message=str(message)
    send_text = 'https://api.telegram.org/bot5032770954:AAEq_ekucF6PG7aOMpF-cSrr_yj_rf1C-Bc/sendMessage?chat_id=1354638378&parse_mode=MarkdownV2&text=' + message 
    b=requests.get(send_text)
    return b

def wait():
    print("no network connection")
    time.sleep(30)

def get_tele_msg():
    a=requests.get('https://api.telegram.org/bot5032770954:AAEq_ekucF6PG7aOMpF-cSrr_yj_rf1C-Bc/getUpdates').text
    a=json.loads(a)
    b=len(a["result"])
    b=b-1
    text=a["result"][b]["message"]["text"]
    text=text.lower()
    id=a["result"][b]["message"]["from"]["id"]
    return (text, id) 

def work():
   text, id=get_tele_msg()
   while id==1354638378:
    send("waiting for your command sir")
    for i in range(1,21):
        print(i,end=" ")
        time.sleep(1)
    print(" ")    
    text, id=get_tele_msg()   
    if 'open chrome' in text and id==1354638378 :
        print("opening chrome")
        webbrowser.open_new("https://www.google.com/")
        send("what do u want to search sir")
        time.sleep(20)
        text, id=get_tele_msg()
        if "search" in text:
            text=text.replace("search","")
            print("opening",text)
            import pywhatkit as pwk
            pwk.search(text)
            send("Do u want something more tell me yes or no")
            time.sleep(10)
            text, id=get_tele_msg()
            if "yes" in text:
                send("Request accepted give me new command")
                work()
            elif "no" in text:
                send("thank you for using me sir")
                break    

            break
        break 
    elif 'shut down' in text and id==1354638378:
        import pywhatkit as pwk
        print("shutting down computer")
        pwk.shutdown(40)
        send("do u really want's to shut down you have only 5 seconds tell me fast")
        for i in range(1,11):
            print(i)
            j=str(i)
            send(j)
            time.sleep(1)
        text, id=get_tele_msg()
        if "cancel shut down" in text and id==1354638378:
            pwk.cancel_shutdown()
            send("shut down has been cancelled successfully")
        else:
            send("your computer is turned off by me")
    
        break
    elif  "exit" == text:
        print("thank you for using me sir ")
        send("Do u want something more tell me yes or no")
        time.sleep(10)
        text, id=get_tele_msg()
        if "yes" in text:
            send("Request accepted give me new command")
            work()
        elif "no" in text:
            send("thank you for using me sir")
            break    
        break
    elif "take photo and send me" in text and id==1354638378:
        import photo_module as p
        p.run()
        send("Do u want something more tell me yes or no")
        time.sleep(10)
        text, id=get_tele_msg()
        if "yes" in text:
            send("Request accepted give me new command")
            work()
        elif "no" in text:
            send("thank you for using me sir")
            break    
        break
    elif "#execute remotely" in text:
        send("request accepted")
        import remote_executer
        import pyautogui as pg
        time.sleep(10)
        pg.screenshot("screenshot.png")
        b=open("screenshot.png",'rb')
        file =  {'photo':b}
        requests.post('https://api.telegram.org/bot5032770954:AAEq_ekucF6PG7aOMpF-cSrr_yj_rf1C-Bc/sendPhoto?chat_id=1354638378&caption=photo from Jarvis',files=file)
        b.close()
        import os
        os.remove("screenshot.png")
        break
    else:
        continue

def startup(wait):
    try:
        message = 'sir your computer has started 2 minutes ago'
        send(message)
        
    except:
        wait()
    finally:
        work()

print('Welcome Sir')

def connect(host='http://google.com'):

    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False

def sec():
    if connect() is True:
        text, id=get_tele_msg()
        startup(wait)  
    else:
        print("no internet")
        time.sleep(30)
        sec()
    return (text,id)        

text,id=sec()    