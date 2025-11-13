import cv2
import pytesseract
import matplotlib.pyplot as plt
import re
import pyautogui
import time
import pyscreeze
from datetime import datetime
from PIL import ImageGrab
from functools import partial

t = datetime.now()
current_time = t.strftime("%D %H:%M:%S:%f")
current_sec = t.strftime("%S")
# current_time = time.strftime("%H:%M:%S", t)

# print(image.shape)
global a
a = []

def read_character(roi_coordinates):
    image = cv2.imread('YOUR IMAGE PATH')

    # Iterate over the ROIs
    for i, (x1, y1, x2, y2) in enumerate(roi_coordinates):
        # Ensure the coordinates are within the image dimensions
        x1 = max(0, x1)
        y1 = max(0, y1)
        x2 = min(image.shape[1], x2)
        y2 = min(image.shape[0], y2)
    
        # Crop the ROI from the image
        roi = image[y1:y2, x1:x2]
    
        # Convert the ROI to grayscale
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

        # Display the grayscale ROI
        # plt.figure()
        # plt.imshow(cv2.cvtColor(gray_roi, cv2.COLOR_GRAY2RGB))
        # plt.axis('off')
        # plt.show()
    
        # Apply image preprocessing if required
        # Example 1: Thresholding
        _, thresholded_roi = cv2.threshold(gray_roi, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
        # Example 2: Denoising (using a bilateral filter)
        denoised_roi = cv2.bilateralFilter(thresholded_roi, 9, 75, 75)
    
        # Perform OCR on the preprocessed ROI using pytesseract
        pytesseract.pytesseract.tesseract_cmd = r'YOUR PYTESSERACT PATH HERE'
        extracted_text = pytesseract.image_to_string(denoised_roi, config='--psm 7')  # Use page segmentation mode 7 for treating the image as a single line of text
        # extracted_text = pytesseract.image_to_string(image)
        
        # Extract numbers from the extracted text
        numbers = re.findall(r'\d+', extracted_text)
        # numbers = f"{'.'.join(numbers)}"
        # a.append(numbers)
        
        # Display the extracted numbers
        if numbers:
            # print(f"Numbers from ROI: {'.'.join(numbers)}")
            b = f"{'.'.join(numbers)}"
            a.append(b)
            # print(b)

        else:
            a.append('0')
            print(f"No numbers found in ROI")
    return a
#Coordinate values to search

# Table on chart
# image_parts = [{'x1':2865, 'y1':1662, 'x2':2895, 'y2':1688},
#                {'x1':2865, 'y1':1692, 'x2':2895, 'y2':1722}]

# image_parts = [{'x1':2865, 'y1':1692, 'x2':2895, 'y2':1722}]

image_parts = [{'x1':0, 'y1':0, 'x2':60, 'y2':30},
               {'x1':0, 'y1':30, 'x2':60, 'y2':60}]

# Data Window
# image_parts = [{'x1':3995, 'y1':1347, 'x2':4041, 'y2':1365},
#                {'x1':3995, 'y1':1365, 'x2':4041, 'y2':1385}]

#Left Side 1 Chart And Data Window Scrolled Fully Down
# image_parts = [{'x1':855, 'y1':258, 'x2':905, 'y2':280},
#                {'x1':855, 'y1':285, 'x2':906, 'y2':308}]

# Define the regions of interest (ROIs) where you want to extract data
def readImage():
    for coordinate in image_parts:
        x1, y1, x2, y2 = coordinate.values()
        roi_coordinates = [
            (x1, y1, x2, y2),  # Format: (top-left x, top-left y, bottom-right x, bottom-right y)
        ]
        read_character(roi_coordinates)
        

# status = 1
# while status == 1:
s = 1
count = 0
long = 0
short = 0
while s == 1:
    start_time = time.time()
    # print(datetime.now())
    # print("Play?")
    # move = input()
    # if move == "1":
    
    current_sec = time.localtime().tm_sec
    print(current_sec)

    if current_sec == 57:
        ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
        # im = pyscreeze.screenshot('testt.png')
        region = (1815, 250, 60, 60)
        # region = (0, 0, 1000, 1000)
        im = pyscreeze.screenshot('testt.png', region)
        readImage()
        print(a)

        if a[0] == "1.00":
            pyautogui.click(x = 762, y = 133)
            pyautogui.click(x = 756, y = 651)
            pyautogui.click(x = 418, y = 133)
            pyautogui.click(x = 419, y = 645)
            print("LongIn", long)
        elif a[1] == "1.00":
            pyautogui.click(x = 842, y = 131)
            pyautogui.click(x = 834, y = 648)
            pyautogui.click(x = 501, y = 135)
            pyautogui.click(x = 493, y = 645)
            print("ShortIn", short)
            
        count = count + 1
        print("Count: ", count)
        a = []
        
    end_time = time.time()
    total_time = end_time - start_time

 






