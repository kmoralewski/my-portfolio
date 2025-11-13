import pyautogui
import time


#Simple automated setup to for my trading windows in the morning


# pyautogui.moveTo(700, 20)  
# pyautogui.dragTo(700, 525, 2)



#Duplicate Tab 1
time.sleep(2)
pyautogui.moveTo(550, 25)  
pyautogui.click(button='right')
time.sleep(2)
pyautogui.click(x=600,y=205)  


#Drag duplicate from 1 to 2
pyautogui.moveTo(590, 25)  
pyautogui.dragTo(960, 25, 2)




#Duplicate Tab 1
time.sleep(2)
pyautogui.moveTo(550, 25)  
pyautogui.click(button='right')
time.sleep(2)
pyautogui.click(x=600,y=205)  

#Drag duplicate from 1 to 2
pyautogui.moveTo(590, 25)  
pyautogui.dragTo(590, 565, 2)




#Duplicate Tab 2
time.sleep(2)
pyautogui.moveTo(565, 565)  
pyautogui.click(button='right')
time.sleep(2)
pyautogui.click(x=640,y=745)  

#Drag duplicate from 3 to 4
pyautogui.moveTo(590, 565)  
pyautogui.dragTo(970, 565, 2)



#Duplicate Tab 1
time.sleep(2)
pyautogui.moveTo(550, 25)  
pyautogui.click(button='right')
time.sleep(2)
pyautogui.click(x=600,y=205)  

#Drag duplicate from 1 to 5
pyautogui.moveTo(590, 25)  
pyautogui.dragTo(1490, 25, 2)

