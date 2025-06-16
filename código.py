import pyautogui
import time

pyautogui.PAUSE = 2
#enter in your browser

pyautogui.press ('win')
pyautogui.write ('Opera Gx')
pyautogui.press ('enter')
time.sleep (10)
#enter on website
pyautogui.click (x = 1004, y = 57)
pyautogui.write ("https://saladofuturo.educacao.sp.gov.br/escolha-de-perfil")
pyautogui.press ("enter")

#wait loading
time.sleep(6)


#make  login
pyautogui.click (x = 1552, y = 633) 
pyautogui.press ("tab")
pyautogui.write ("000113516899")
pyautogui.press ("tab")
pyautogui.write ("4")
pyautogui.press ("tab")
pyautogui.press ("tab")
pyautogui.press ("tab")
pyautogui.write ("Lui2009@")
pyautogui.press ('tab')
pyautogui.press ("tab")
pyautogui.press ("tab")
pyautogui.press ("tab")
pyautogui.press ('enter')

time.sleep (6)
#enter in khan academy

pyautogui.scroll (-1000)
pyautogui.click (x = 1269, y = 748)

time.sleep (20)

#get the lesson

pyautogui.click (x = 417, y = 135)
pyautogui.scroll (-300)
time.sleep (6)

pyautogui.click (x= 1403, y = 494)
time.sleep (2)
pyautogui.click (x = 116, y = 84)
time.sleep (10)

pyautogui.click (x = 889, y = 466)
time.sleep (2)
pyautogui.click (x = 1841, y = 1014)    

#end of code











