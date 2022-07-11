import imp
import time
import pyautogui
import os
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

shot=None
shot=pyautogui.locateCenterOnScreen("mass\shot.png")
if shot is not None:
    print ('shot found')
    pyautogui.moveTo(shot)
    time.sleep(2)
    pyautogui.click(shot)
    time.sleep(2)
    #os.system('python selectall.py -W ignore::DeprecationWarning')
    exec(open("selectall.py").read())
else:
    print ('shot not FOUND \n next python selectall.py ')
    exit()