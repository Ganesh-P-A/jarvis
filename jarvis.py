#                                                           Made By Ganesh                                                                   
#                                                           Jarvis Mark-II                                                                   
print('user verification required')
import json
import cv2
#import photo_module
def modules():                                                                                                  #if error then reinstall modules
    # Program Made By Ganesh 
    import pyttsx3
    import speech_recognition as sr
    import datetime
    import os
    import wikipedia
    import webbrowser
    import sys
    import pyautogui
    import time 
    import pywhatkit as pwk
    import json
    import socket  
    #import pyjokes
    import random
    import requests
     
    
    return pyttsx3,sr,datetime,os,wikipedia,webbrowser,sys,pyautogui,time,pwk,socket,random, requests,json
pyttsx3, sr, datetime, os, wikipedia, webbrowser, sys, pyautogui, time, pwk, socket, random, requests, json = modules()

def start():                                                                                                    #for voice
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',190)
    return engine
engine = start()

def speak(audio):                                                                                               #for voice
    engine.say(audio)
    engine.runAndWait()
    
def takecommand():                                                                                              # taking commands for jarvis
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=None,phrase_time_limit=None)        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in').lower()
        print("User said:", query)
    except Exception as e: 
        print("waiting for your command")
        return "None"
        
    return query

def ti():                                                                                                       #for Getting time to Jarvis
        Ti = datetime.datetime.now().strftime("%I:%M:%S")
        return Ti     

def get_tele_msg():
    a=requests.get('https://api.telegram.org/bot5032770954:AAEq_ekucF6PG7aOMpF-cSrr_yj_rf1C-Bc/getUpdates').text
    a=json.loads(a)
    b=len(a["result"])-1
    message=a["result"][b]["message"]["text"]
    name=a["result"][b]["message"]["chat"]["username"]
    return (message,name)

def send(message):
    a=requests.get(f"https://api.telegram.org/bot5032770954:AAEq_ekucF6PG7aOMpF-cSrr_yj_rf1C-Bc/sendMessage?chat_id=1354638378&parse_mode=MarkdownV2&text={message}")
    return (a)

def TaskExecution():                                                                                            #executing various tasks
    while True:
        query = takecommand()
        if 'wikipedia' in query:
                speak('Searching wikipedia...')
                queryy = query.replace("wikipedia","")
                results = wikipedia.summary(queryy, sentences=2)
                print(results)
                speak(f'according to wikipedia {results}')
        elif 'who is' in query or 'what is mean by' in query:
                speak("searching on google")
                pwk.search(query)
        elif 'open youtube' in query:
                speak("opening youtube")    
                webbrowser.open('https://www.youtube.com')
                query1 = takecommand()
                if 'search' in query1:
                        query11 = query1.replace('search','')
                        pwk.playonyt(query11)
                elif 'hey jarvis' in query1:
                        break 
                else:
                        query1=query
                        break
                                
        elif 'open facebook' in query:
                speak("opening facebook")
                webbrowser.open('https://www.facebook.com')           

        elif 'open chrome' in query:
                speak("opening google chrome")
                chrome =  "C:\Program Files\Google\Chrome\Application\chrome.exe"
                os.startfile(chrome)

        elif 'open vs code' in query:
                speak("opening vs code")
                vs =  "C:/Microsoft VS Code/Code.exe"
                os.startfile(vs)        
            
        elif 'close chrome' in query or 'close facebook' in query or 'close youtube' in query:
                speak("closing chrome")
                chrome =  "C:\Program Files\Google\Chrome\Application\chrome.exe"
                os.system("taskkill /f /im  chrome.exe")         
        elif 'close' in query:
                close = query.replace('close','')
                os.system(f"taskkill /f /im  {close}.exe") 
        elif 'time' in query:
                Ti = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir,the time is {Ti}")

        elif 'who are you' in query:
                intro = "C:/jarvis ready/jarvis intro.mp4"
                os.startfile(intro)
                time.sleep(20)
                pyautogui.keyDown("alt")
                pyautogui.press('tab',presses=1)
                time.sleep(1)
                pyautogui.keyUp("alt") 
                
        elif 'play song' in query:
                speak("playing song")
                webbrowser.open('https://www.youtube.com/results?search_query=songs')       

        elif 'open whatsapp' in query:
                speak("opening whatsapp")
                os.startfile('C:/Users/ganesh/AppData/Local/WhatsApp/WhatsApp.exe')
            
        elif 'change window' in query:
                speak("switching window")
                pyautogui.keyDown("alt")
                pyautogui.press('tab',presses=1)
                time.sleep(1)
                pyautogui.keyUp("alt")
                
        elif 'you may leave' in query:
                speak(" thank you for using me sir") 
                break

        elif 'who made you' in query:
                speak("   i am originally made by tony stark,but now recreated by Ganesh i am not controlling ganesh's computer ")    

        elif 'close chrome' in query:
                speak("closing chrome")
                chrome =  "C:\Program Files\Google\Chrome\Application\chrome.exe"
                os.system("taskkill /f /im  chrome.exe")

        elif 'exit' in query:
                speak("        thank you for using me sir") 
                sys.exit() 
                
        elif 'thank you' in query:
                speak("        thank you for using me sir") 
                break 
                
        elif 'wait jarvis' in query:
                speak("waiting for next 30 seconds")
                time.sleep(30)
                for i in range(30,0,-1):
                 time.sleep(1)
                speak(i)
                
        elif 'reading' in query or 'open acrobat' in query:
                speak('opening acrobat')   
                os.startfile("C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe")
        elif 'check my ip' in query:
                hostname = socket.gethostname()   
                IPAddr = socket.gethostbyname(hostname)   
                speak("Your Computer Name is:" + hostname)   
                speak("Your Computer IP Address is:" + IPAddr)    
        elif 'sleep' in query:
                speak("        thank you for using me sir") 
                break
            
        elif 'stop' in query:
                speak("        thank you for using me sir") 
                sys.exit()  
        
        elif 'shut down my system' in query:
                speak("   your computer will shutdown in next 10 seconds") 
                send_text = 'your system is now turned off by me'
                send(send_text)
                speak("thank you for using me sir")
                time.sleep(1)
                pwk.shutdown(3)
                sys.exit()

        elif 'random one to hundred' in query:
                ran = random.randint(1, 100)
                speak(ran)
                
        elif 'random 1 to 10' in query:
                ran = random.randint(1, 10)
                speak(ran)    
                
                query = takecommand().lower()
                if 'again' in query:
                 ran = random.randint(1, 10)
                speak(ran)  
            
        elif 'on youtube' in query:
                search = query.replace("on youtube","")
                pwk.playonyt(search)
                 
        elif 'on google' in query:
                search1 = query.replace("on google","")
                pwk.search(search1)

        elif 'web search' in query:
                ws = query.replace("web search","")
                webbrowser.open(f'https://www.{ws}.com')
        
        elif 'take screenshot' in query:
                
                Ti = datetime.datetime.now().strftime("%I:%M:%S:%D")
                Time = Ti.replace(':','')
                name = Time.replace('/','')
                img = pyautogui.screenshot()
                img.save(f"{name }.png")
                os.startfile(f"G:/jarvis ready/{name }.png") 
        
        elif 'write' in query or 'right' in query or 'note' in query:
              speak("taking note")
              Ti = datetime.datetime.now().strftime("%I:%M:%S:%D")
              Time = Ti.replace(':','')
              name = Time.replace('/','')
              ttw = query.replace("bright write right","")
              pwk.text_to_handwriting(ttw, f"G:/jarvis ready/jarvis handwriting/{name}.png", (0, 0, 138)) 
              print(ttw)
              os.startfile(f"G:/jarvis ready/jarvis handwriting/{name}.png")     

        elif 'how are you' in query:
                speak("i am fine sir") 
       
        elif 'open powerpoint' in query:
               os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office 2013/PowerPoint 2013")

        elif 'close powerpoint' in query:
                os.system("taskkill /f /im  PowerPoint 2013")

        elif 'close acrobat' in query:
                os.system("taskkill /f /im  Acrobat.exe")
        
        elif 'open excel' in query:
              os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office 2013/Excel 2013")    
        
        elif 'close excel' in query:
               os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office 2013/Excel 2013")                   

        elif 'open gta vice city' in query or 'open gta' in query or 'open game' in query:
                os.startfile("C:/gta vice city/gta-vc.exe")   
        
        elif 'wait and sleep' in query or 'exit and sleep' in query:
                speak('closing program jarvis')
                break      
        
        elif 'change tab' in query:
                speak('changing chrome tab')
                pyautogui.keyDown('ctrlright')
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.keyUp('ctrlright')
        
        elif 'make new tab' in query:
                speak('opening chrome tab')
                pyautogui.keyDown('ctrlright')
                pyautogui.press('t')
                time.sleep(1)
                pyautogui.keyUp('ctrlright')
                
        elif 'working music' in query:
                webbrowser.open('https://www.youtube.com/watch?v=bcyvZIoQp9A')        
        
         #'''elif 'volume up' or 'volumeup' or 'increase sound' or 'increase volume' in query:
                #pyautogui.press('volumeup',presses=3)
        
         #elif 'volume down' or 'volumedown' or 'decrease sound' or 'decrease volume' in query:
                #pyautogui.press('volumedown',presses=3)

         #elif 'volume mute' or 'volumemute' or 'mute sound' or 'mute volume' or 'mute' in query:
                #pyautogui.press('volumemute')
        
         #elif 'volume full' or 'volumefull' or 'full sound' or 'full volume' in query:
                #pyautogui.press('volumeup',presses=50)'''                
        
        elif 'on chrome' in query:
                speak('opening Chrome')
                openu = query.replace("on chrome","")
                webbrowser.open(openu)
                
        elif 'what can you do' in query:
               os.startfile("C:/jarvis ready/what can you do.txt")
               print('for stop my speaking press ctrl + C')
               speak(''''searching on wikipedia
               opening youtube,facebook,whatsapp,chrome,powerpoint,gta vc,acrobat,college at rank
               closing chrome
               telling time
               ask who are you
               playing song
               changing window
               checking ip
               jokes
               shutting down system
               random 1to 100 or random 1 to 10
               searching on youtube or searching on google
               taking screenshot''')
               speak('for closing me say wait and sleep')
               time.sleep(2)
               os.system("taskkill /f /im  notepad.exe") 
        
        elif 'open router settings' in query:
                speak('opening chrome')
                webbrowser.open('192.168.1.1')

        elif 'monkey mode' in query:
                speak("speak starting monkey mode")
                monkeymode()

        elif 'exit monkey mode' in query:
                return TaskExecution()

        
        elif 'dog' in query:
                speak('lets see who is good dog??')
                os.startfile('C:/jarvis ready/Barking Dog Sms Tone.mp3')
                time.sleep(6)
                pyautogui.keyDown("alt")
                pyautogui.press('tab',presses=1)
                time.sleep(1)
                pyautogui.keyUp("alt")

        elif 'close whatsapp' in query:
                os.system("taskkill /f /im  WhatsApp.exe")     
       
        elif 'print document' in query:
              pyautogui.keyDown("ctrlright")
              pyautogui.press("p")
              time.sleep(1)
              pyautogui.keyUp("ctrlright")

        elif 'print' in query:
                out = query.replace("print","")
                print(out) 

        elif 'send photo' in query:
              continue
              photo= askopenfilename(title="Select a File", filetype=(('image','*.png'),('all files','*.*'))) or "G:/jarvis ready/1.png"
              send(photo=photo)
        
        elif 'open notepad' in query:
                os.startfile('C:/jarvis ready/notepad.exe')
        
        elif 'press' in query:
                but = query.replace('press','')
                time.sleep(2)
                print(but)
                pyautogui.press(f'{but}')
        
        elif 'anaconda' in query:
                os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)\Anaconda Navigator (Anaconda).lnk')
        
        elif 'teams' in query:
                os.startfile('C:/Users/ganesh/AppData/Local/Microsoft/Teams/Update.exe')

        elif 'wake up jarvis' in query:
                pyautogui.press('space')
        elif 'new messages' in query:
                message,name=get_tele_msg()
                speak(f"{message} from {name}")
        elif "send me my photo" in query:
                photo_module.run()        

def greetings():  
    speak('recognition successful')
    speak('welcome Back Sir')
    #startup()
    send(f"sir jarvis intiated on your computer at time {ti()}")
    WishMe() 
    TaskExecution()      
       
def WishMe():                                                                                                   # wishing 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")  
    else:
        speak ("Good evening!")

def monkeymode():                                                                                               #jarvis works like talking tom
       while True:
        reapeat = takecommand()
        if 'exit monkey mode' in reapeat or 'exit' in reapeat:
                speak('closing monkey mode')
                TaskExecution()
                break
        else:
                speak(reapeat)
                continue

def wakeup(speak, TaskExecution):
    speak('user verification required')
    recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
    recognizer.read('trainer/trainer.yml')   #load trained model
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

    font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type

    id = 2 #number of persons you want to Recognize

    names = ['','Ganesh']  #names, leave first empty bcz counter starts from 0

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
    cam.set(3, 640) # set video FrameWidht
    cam.set(4, 480) # set video FrameHeight


    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)



    while True:
        ret, img =cam.read() #read the frames using the above created object

        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

        faces = faceCascade.detectMultiScale( 
        converted_image,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) 

            id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) 

        
            if (accuracy < 100):
                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))
                k = cv2.waitKey(10) & 0xff 
                cam.release()
                cv2.destroyAllWindows() 
                pyautogui.press('escape')
                greetings()
                
            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))
                speak('user not recognised')
            

            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
        cv2.imshow('camera',img) 

        k = cv2.waitKey(10) & 0xff 
        if k == 27:
            break

    cam.release()
    cv2.destroyAllWindows()  
        
wakeup(speak, TaskExecution) 
#                                                             End of Code of Jarvis
