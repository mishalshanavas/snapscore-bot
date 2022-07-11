import pyautogui
import time
import os
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


time.sleep(1)
selectall=None
selectall=pyautogui.locateCenterOnScreen("mass\selectall.png")
if selectall is not None:
    print("selectall found")
    pyautogui.moveTo(selectall)
    time.sleep(1)
    pyautogui.click(selectall)
    time.sleep(1.5)
    #os.system('python send.py -W ignore::DeprecationWarning')
    exec(open("send.py").read())
else:
    print("selectall not found \n next python send.py")
    exit()