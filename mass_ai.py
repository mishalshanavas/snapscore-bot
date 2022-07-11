# scrcpy --max-fps 15 -w scrcpy -b 2M -m 1000 --lock-video-orientation=1

import pyautogui
import time

for i in range(50):
    print('starting')
    snapmulti = None 
    snapmulti=pyautogui.locateCenterOnScreen("mass\snapmulti.png")
    if snapmulti is not None:
        for j in range(8):
            pyautogui.click(snapmulti) 
            time.sleep(1.5)
   
        #multisnap full
        time.sleep(1.5)
        snapfull=None
        snapfull=pyautogui.locateCenterOnScreen("mass\snapfull.png")
        
        if snapfull is not None:
            print('multisnap full')
            pyautogui.click(snapfull)
            time.sleep(1)
            pyautogui.click(snapfull)
            time.sleep(2)

        else:
            print('snap was not full')
            exit()
        
        tick=None
        time.sleep(3)
        tick=pyautogui.locateCenterOnScreen("mass\tick.png" , region = (1145, 40, 65, 80))
        if tick is not None:
            print("ticck found")
            pyautogui.click(tick)
            time.sleep(2)
        else:
            print ('tick was not found')
            

        #sendto
        sendto=None
        time.sleep(1.5)
        sendto=pyautogui.locateCenterOnScreen ("mass\sendto.png")
        if sendto is not None:
            print('sendto found')
            pyautogui.click(sendto)
            time.sleep(2)
        else:
            print('send to not found')
            exit()

        #find shortchut

        shot=None
        shot=pyautogui.locateCenterOnScreen("mass\shot.png")
        if shot is not None:
            print ('shot found')
            pyautogui.moveTo(shot)
            time.sleep(2)
            pyautogui.click(shot)
            time.sleep(2)

            #selectall
            time.sleep(3)
            selectall=None
            selectall=pyautogui.locateCenterOnScreen("mass\selectall.png")
            if selectall is not None:
                print("selectall found")
                pyautogui.moveTo(selectall)
                time.sleep(1)
                pyautogui.click(selectall)
                time.sleep(4)
            else:
                print("selectall not found")
                exit()
            
            #send
            send=None
            send=pyautogui.locateCenterOnScreen("mass\send.png")
            if send is not None:
                print('send found')
                pyautogui.moveTo(send)
                time.sleep(1)
                pyautogui.click(send)
                time.sleep(30)
            else:
                print('send not found')
                exit()

            # camera 
            camera=None
            camera=pyautogui.locateCenterOnScreen("mass\camera.png")
            if camera is not None:
                print("camera found")
                pyautogui.moveTo(camera)
                time.sleep(1)
                pyautogui.click(camera)
                time.sleep(2)
            else:
                print("camera not found")
                exit()     
        else:
            print ('shot not FOUND')
            exit()
    else:
        print('multi snap not found or not in screen')
        exit()    


