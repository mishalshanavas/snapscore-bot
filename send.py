import pyautogui
import time
import os
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


send=None
send=pyautogui.locateCenterOnScreen("mass\send.png")
if send is not None:
    print('send found')
    pyautogui.moveTo(send)
    time.sleep(1)
    pyautogui.click(send)
    time.sleep(20)
    #os.system('python camera.py -W ignore::DeprecationWarning')
    exec(open("camera.py").read())
else:
    print('send not found \n next python camera.py')
    exit()
