import pyautogui, time

#Simple clicker to keep trading windows active

while True:
    current_sec = time.localtime().tm_sec
    if current_sec == 45:
        pyautogui.click(x = 1071, y =106)
        pyautogui.click(x = 1570, y =108)
        pyautogui.click(x = 1072, y =637)
        pyautogui.click(x = 1569, y =634)
        time.sleep(150)