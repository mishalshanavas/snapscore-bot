#scrcpy --max-fps 24 -w -b 2M -m 1000 --lock-video-orientation=1
import pyautogui
import time
import os
import subprocess

i=1
j=1
o=False
t=0
snap_send=0
snap_count=0
while(i==1):
    time.sleep(t)

    result = subprocess.run(['adb', 'shell', 'dumpsys', 'battery'], capture_output=True, text=True)
    temperature_line = [line for line in result.stdout.split('\n') if 'temperature' in line]
    temperature = temperature_line[0].split(':')[1].strip()
    print(temperature)
    temp=int(temperature)
    if temp>=320:
        print ("phone is hot let it cool")
        time.sleep(500)
    print("total snapsent : " ,snap_count ," tempatarure is " , temp )

    
    if j>=5 & o != True :
        os.system("start /B start cmd.exe @cmd /k scrcpy --max-fps 24 -w -b 2M -m 1000 --lock-video-orientation=1")
        j=0
        o=True
        time.sleep(10)
    
    bluetick = pyautogui.locateCenterOnScreen('bluetick.png', grayscale=True, confidence=.9)
    print(bluetick)

    snap_button_m = pyautogui.locateCenterOnScreen('snap_button_m.png', grayscale=True, confidence=.9)
    print(snap_button_m)

    ok_button = pyautogui.locateCenterOnScreen('ok_button.png', grayscale=True, confidence=.9)
    print(ok_button)

    send_button_first = pyautogui.locateCenterOnScreen('send_button_first.png', grayscale=True, confidence=.9)
    print(send_button_first)

    shortcut_emoji = pyautogui.locateCenterOnScreen('shortcut_emoji.png', grayscale=False)
    print(shortcut_emoji)

    select_all = pyautogui.locateCenterOnScreen('select_all.png', grayscale=True, confidence=.9)
    print(select_all)

    send_button_last = pyautogui.locateCenterOnScreen('send_button_last.png', grayscale=True, confidence=.9)
    print(send_button_last)
 
    camera_button = pyautogui.locateCenterOnScreen('camera_button.png', grayscale=True, confidence=.9)
    print(camera_button)



    if ok_button != None:
        pyautogui.click(ok_button)
        t=0.04
        ok_button=None
    elif snap_button_m != None:
        pyautogui.click(snap_button_m)
        t=0.02
        snap_button=None
    elif bluetick != None:
        pyautogui.click(bluetick)
        bluetick=None
    elif send_button_first != None:
        pyautogui.click(send_button_first)
        send_button=None
    elif shortcut_emoji != None:
        pyautogui.click(shortcut_emoji)
        shortcut_emoji=None
    elif select_all != None:
        pyautogui.click(select_all)
        select_all=None
    elif send_button_last != None:
        pyautogui.click(send_button_last)
        send_button_last=None
        snap_count=snap_count+1
        print(snap_count,"snaps send")
    elif camera_button != None:
        pyautogui.click(camera_button)
        camera_button=None
    else:
        print('fuckyou')
        j=j+1
        
