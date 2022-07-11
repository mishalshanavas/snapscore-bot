import pyautogui
import time
import os
import warnings



camera=None
camera=pyautogui.locateCenterOnScreen("mass\camera.png")
if camera is not None:
    print("camera found")
    pyautogui.moveTo(camera)
    time.sleep(1)
    pyautogui.click(camera)
    time.sleep(2)
    #os.system('python snapmulti.py -W ignore::DeprecationWarning')
    exec(open("snapmulti.py").read())
else:
    print("camera not found \n next python snapmulti.py")
    exit()  