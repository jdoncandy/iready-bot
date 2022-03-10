import pyautogui
import time

time.sleep(5)

#var = pyautogui.locateCenterOnScreen('text.png')

#pyautogui.click(var)

#print("sup")

def bot(img):
    var = pyautogui.locateCenterOnScreen(img)

    if var == None:
        onscreen = False
    
    else:
        onscreen = True
    print(var)
    return onscreen




if bot('text.png') == True:
    print("lets go")

else:
    print("not on screen")
    
