import pyautogui
import time
import keyboard
import webbrowser


pozitie_initiala_x = 512
pozitie_initiala_y = 390
pos_fin_x=1656
pos_fin_y=780
dif_x=889-pozitie_initiala_x
dif_y=pos_fin_y-pozitie_initiala_y
curent_x=512
curent_y=390

def autoviwe(curent_x,pos_fin_x,pozitie_initiala_x,pozitie_initiala_y,dif_x,curent_y,dif_y,pos_fin_y):
    time.sleep(1)
    while not keyboard.is_pressed('esc'):
        time.sleep(1)
        if curent_x<=pos_fin_x :
            pyautogui.click(curent_x,curent_y)
            print(1,curent_x,curent_y)
            curent_x=curent_x+dif_x
            time.sleep(3)
            if pyautogui.locateOnScreen(r'C:\Users\Nick\OneDrive\Desktop\Back_butt.png' , confidence=0.7)!= None:
                #camp_google=pyautogui.locateOnScreen(r'C:\Users\Nick\OneDrive\Desktop\Back_butt.png' , confidence=0.7)
                pyautogui.click(pyautogui.locateOnScreen(r'C:\Users\Nick\OneDrive\Desktop\Back_butt.png' , confidence=0.7))
        else:
            curent_x=pozitie_initiala_x
            time.sleep(1)
            pyautogui.move(curent_x,curent_y)
            pyautogui.scroll(-83)
            time.sleep(4)   
webbrowser.open("https://www.youtube.com/")
time.sleep(5)           
autoviwe(curent_x,pos_fin_x,pozitie_initiala_x,pozitie_initiala_y,dif_x,curent_y,dif_y,pos_fin_y)

def cautare_google():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'C:\Users\Nick\OneDrive\Desktop\Cod.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'C:\Users\Nick\OneDrive\Desktop\Cod.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write('https://youtube.com')
        pyautogui.press('enter')
    else:
        print("Imaginea nu este pe ecran")

def cautare_youtube():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'C:\Users\Nick\OneDrive\Desktop\Cod2.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'C:\Users\Nick\OneDrive\Desktop\Cod2.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write('life of boris')
        pyautogui.press('enter')
    else:
        print("Imaginea nu este pe ecran")

def cautare_boris():
    time.sleep(5)
    if pyautogui.locateOnScreen() != None:
        camp_google = pyautogui.locateOnScreen(r'C:\Users\Nick\OneDrive\Desktop\cod3_boris.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
    else:
        print("Imaginea nu este pe ecran")

def cautare_subscribe():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'C:\Users\Nick\OneDrive\Desktop\cod4_subscribe.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'C:\Users\Nick\OneDrive\Desktop\cod4_subscribe.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
    else:
        print("Imaginea nu este pe ecran")    

def coordonate():        
 print(pyautogui.position())

col = 1
while not keyboard.is_pressed('esc'):
   coordonate()




#cautare_google()
#cautare_youtube()
#cautare_boris()
#cautare_subscribe()
