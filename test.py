import pyautogui

x =pyautogui.locateAllOnScreen("mass/kluetick.png")
for i in x:
    print(i)