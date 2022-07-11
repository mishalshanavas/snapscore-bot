import pyautogui
import time


print('starting')

snapmulti = None 
snapmulti=pyautogui.locateCenterOnScreen("mass\snapmulti.png" , confidence=0.9)
if snapmulti is not None:
    snapfullokbox=None
    while snapfullokbox==None:
        snapfullokbox=pyautogui.locateCenterOnScreen("mass\okbox.png")    
        pyautogui.click(snapmulti) 
        time.sleep(0.8)
    #os.system('python snapfull.py -W ignore::DeprecationWarning')
    exec(open("snapfull.py").read())

else:
        print('multi snap not found or not in screen \n  next python snapfull.py')
        exit()  
