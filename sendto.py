import pyautogui
import time
import os
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

sendto=None
time.sleep(1.5)
sendto=pyautogui.locateCenterOnScreen ("mass\sendto.png")
if sendto is not None:
    print('sendto found')
    pyautogui.moveTo(sendto)
    time.sleep(1)
    pyautogui.click(sendto)
    time.sleep(1.5)
    #os.system('python shot.py -W ignore::DeprecationWarning')
    exec(open("shot.py").read())
else:
    print('send to not found \n next python shot.py')
    exit()
