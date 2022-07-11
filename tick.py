import pyautogui
import time
import os
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

tick=None
time.sleep(3)
tick=pyautogui.locateCenterOnScreen("mass\kluetick.png" , region = (1145, 40, 65, 80) , confidence=0.9)
if tick is not None:
    print("tick found")
    pyautogui.moveTo(tick)
    time.sleep(1)
    pyautogui.click(tick)
    time.sleep(1.5)
    #os.system('python sendto.py -W ignore::DeprecationWarning')
    exec(open("sendto.py").read())
else:
    print ('tick was not found \n next python sendto.py')
    os.system('python sendto.py')