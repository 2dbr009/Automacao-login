import pyautogui
import time

pyautogui.PAUSE = 2
#enter in your browser

pyautogui.press ('win')
pyautogui.write ('chrome') #or input your browser name
pyautogui.press ('enter')
time.sleep (10)
#enter on emprise system
#pyautogui.write ("URL site")
pyautogui.press ("enter")

#wait loading
#time.sleep(5)


#make  login
#pyautogui.click (x = 932, y = 459) #modify of your text input posicion
#pyautogui.write ("your login")
#pyautogui.press ("tab")
#pyautogui.write ("your password")
#pyautogui.press ('tab')
#pyautogui.press ('enter')