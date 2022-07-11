import pyautogui
import time
import os
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

time.sleep(1.5)
snapfull=None
snapfull=pyautogui.locateCenterOnScreen("mass\snapfull.png")

if snapfull is not None:
    print('multisnap full')
    pyautogui.click(snapfull)
    time.sleep(1)
    pyautogui.click(snapfull)
    time.sleep(1.5)
    #os.system('python tick.py -W ignore::DeprecationWarning')
    exec(open("tick.py").read())
else:
    print('snap was not full \n next python tick.py')
    exit()