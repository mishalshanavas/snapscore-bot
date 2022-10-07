import pyautogui
import time


for i in range(1000000):
    start_time = time.time()
    
    msg_numb = i
    pyautogui.alert('This is an alert box.')

    def  exiting():
        print(msg)      
        print ("exiting")
        exiting()

    print('starting \n scrcpy --max-fps 15 -w  -b 2M -m 1000 --lock-video-orientation=1  --turn-screen-off')
    def _snap_button_():
        snap_button = None 
        snap_button=pyautogui.locateCenterOnScreen("mass\snap_button.png" , confidence=0.9)
        if snap_button is not None:
            snapfull_ok_box=None
            while snapfull_ok_box==None:
                snapfull_ok_box=pyautogui.locateCenterOnScreen("mass\snapfull_ok_box.png")    
                pyautogui.click(snap_button) 
                time.sleep(0.1)
            
            time.sleep(1)
            snapfull=None
            snapfull=pyautogui.locateCenterOnScreen("mass\snapfull.png")

            while snapfull is not None:
                print('multisnap full')
                pyautogui.click(snapfull)
                time.sleep(0.7)
                snapfull=pyautogui.locateCenterOnScreen("mass\snapfull.png")

                


            sendto=None
            time.sleep(1)
            sendto=pyautogui.locateCenterOnScreen ("mass\sendto.png")
            if sendto is not None:
                print('sendto found')
                pyautogui.moveTo(sendto)
                time.sleep(0.5)
                pyautogui.click(sendto)
                time.sleep(1.2)
                #os.system('python shot.py -W ignore::DeprecationWarning')
                shot=None
                shot=pyautogui.locateCenterOnScreen("mass\shot.png")
                if shot is not None:
                    print ('shot found')
                    pyautogui.moveTo(shot)
                    time.sleep(0.5)
                    pyautogui.click(shot)
                    time.sleep(1.7)
                    #os.system('python selectall.py -W ignore::DeprecationWarning')
                    time.sleep(0.5)
                    selectall=None
                    selectall=pyautogui.locateCenterOnScreen("mass\shot.png")
                    if selectall is not None:
                        print("selectall found")
                        pyautogui.moveTo(selectall)
                        time.sleep(0.5)
                        pyautogui.click(selectall)
                        time.sleep(1.5)


                        selectall = None
                        selectall = pyautogui.locateCenterOnScreen('mass\selectall.png')
                        if selectall is not None:
                            print("selectall found")
                            time.sleep(0.5)
                            pyautogui.click(selectall)
                        else:
                            print('no prob')
                        
                        send=None
                        send=pyautogui.locateCenterOnScreen("mass\send.png")
                        if send is not None:
                            print('send found')
                            pyautogui.moveTo(send)
                            time.sleep(1)
                            pyautogui.click(send)
                            time.sleep(3)
                            #os.system('python camera.py -W ignore::DeprecationWarning')
                            camera=None
                            camera=pyautogui.locateCenterOnScreen("mass\camera.png")
                            if camera is not None:
                                print("camera found")
                                pyautogui.moveTo(camera)
                                time.sleep(0.75)
                                pyautogui.click(camera)
                                time.sleep(1)
                                #os.system('python snap_button.py -W ignore::DeprecationWarning')
                                print(i)
                                print("--- %s seconds ---" % (time.time() - start_time))
                                with open('readme.txt', 'w') as f:
                                    f.write(("\n--- %s seconds ---" % (time.time() - start_time)))



                            else:
                                print("camera not found \n next python snap_button.py")
                                msg =   ("camera not found ")
                                
                        else:
                            print('send not found \n next python camera.py')
                            msg =   ("send not found ")
                            
                    else:
                        print("selectall not found \n next python send.py")
                        msg =   ("selectall not found ")
                        
                else:
                    print ('shot not FOUND \n next python selectall.py ')
                    msg =   ('shot not FOUND  ')
                    
            else:
                print('send to not found \n next python shot.py')
                msg =   ('send to not found ')
                
        else:
            print('snap was not full \n next python tick.py')
            msg =   ("snap was not full ")
    
         
else:
        print('multi snap not found or not in screen \n  next python snapfull.py')
        msg =   ("multi snap not found or not in screen ")
          


_snap_button=pyautogui.locateCenterOnScreen("mass\snap_button.png" , confidence=0.9)
_snapfull_ok_box=pyautogui.locateCenterOnScreen("mass\snapfull_ok_box.png")
_tick=pyautogui.locateCenterOnScreen("mass\kluetick.png")
_sendto=pyautogui.locateCenterOnScreen ("mass\sendto.png")
_shot=pyautogui.locateCenterOnScreen("mass\shot.png")
_selectall=pyautogui.locateCenterOnScreen("mass\selectall.png")
_send=pyautogui.locateCenterOnScreen("mass\send.png")
_camera=pyautogui.locateCenterOnScreen("mass\camera.png")

