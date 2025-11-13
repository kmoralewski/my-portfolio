import mss
import cv2, time, pyautogui
import numpy as np

start_time = time.time()


# Define screen region (adjust coordinates for your setup)
region1 = {"top": 83, "left": 55, "width": 1819, "height": 869}
region2 = {"top": 83, "left": 55, "width": 1819, "height": 860}


def capture_region(region, filename):
    with mss.mss() as sct:
        screenshot = sct.grab(region1)
        img = np.array(screenshot)[:, :, :3]
        cv2.imwrite(filename, img)
        return img


    

time.sleep(3)    
img1 = capture_region(region1, "img1.png")
#cv2.imshow("Captured Region", img1)
#cv2.waitKey(0) 



pyautogui.click(x=348, y=15)


img2 = capture_region(region2, "img2.png")
#cv2.imshow("Captured Region", img2)
#cv2.waitKey(0) 


pyautogui.click(x=92, y=19)

time.sleep(1)
#VM
# pyautogui.click(x=560, y=1060)
#D
pyautogui.click(x=124, y=1059)

time.sleep(1)
pyautogui.click(x=787, y=984)
time.sleep(1)
pyautogui.click(x=828, y=936)
time.sleep(1)
pyautogui.click(x=296, y=498)
time.sleep(1)
pyautogui.typewrite("img1.png")
pyautogui.click(x=787, y=531)


time.sleep(1)
pyautogui.click(x=787, y=984)
time.sleep(1)
pyautogui.click(x=828, y=936)
time.sleep(1)
pyautogui.click(x=296, y=498)
time.sleep(1)
pyautogui.typewrite("img2.png")
pyautogui.click(x=787, y=531)

time.sleep(2)

pyautogui.click(x=836, y=942)
time.sleep(1)
pyautogui.typewrite("-- Prompt to generate a detailed analysis -- ")
time.sleep(1)
#VM
# pyautogui.click(x=513, y=1061)
#D
pyautogui.click(x=163, y=1051)


end_time = time.time()
total_time = end_time - start_time


print(total_time)