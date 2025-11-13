import pandas as pd
import time
import pyautogui
import cv2
import pytesseract
import matplotlib.pyplot as plt
import re
import pyscreeze
from datetime import datetime
from PIL import ImageGrab, Image
from functools import partial

def write1(x):
    nqdd = '2.csv'
    with open(nqdd, "a") as outff:
        print(x, file = outff)

def write2(x):
    nqdd = '3.csv'
    with open(nqdd, "a") as outff:
        print(x, file = outff)

def write3(x):
    nqdd = '4.csv'
    with open(nqdd, "a") as outff:
        print(x, file = outff)

def write4(x):
    nqdd = '5.csv'
    with open(nqdd, "a") as outff:
        print(x, file = outff)

def write5(x):
    nqdd = '6.csv'
    with open(nqdd, "a") as outff:
        print(x, file = outff)

def write6(x):
    nqdd = '7.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write7(x):
    nqdd = '8.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write8(x):
    nqdd = '9.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write9(x):
    nqdd = '10.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write10(x):
    nqdd = '11.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write11(x):
    nqdd = '12.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write12(x):
    nqdd = '13.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write13(x):
    nqdd = '14.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write14(x):
    nqdd = '15.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write15(x):
    nqdd = '16.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write16(x):
    nqdd = '17.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write17(x):
    nqdd = '18.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write18(x):
    nqdd = '19.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write19(x):
    nqdd = '20.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write20(x):
    nqdd = '21.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write21(x):
    nqdd = '22.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write22(x):
    nqdd = '23.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write23(x):
    nqdd = '24.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write24(x):
    nqdd = '25.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write25(x):
    nqdd = '26.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write26(x):
    nqdd = '27.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write27(x):
    nqdd = '28.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write28(x):
    nqdd = '29.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write29(x):
    nqdd = '30.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)

def write30(x):
    nqdd = '31.csv'
    with open(nqdd, "a") as outff:
        print(x, file=outff)


start_time = time.time()


# print(image.shape)
global a
a = []

def read_character(roi_coordinates):

    image = cv2.imread('YOUR IMAAGE PATH HERE')

    # Iterate over the ROIs
    pic = 0
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
        # save = roi_coordinates[i]
        # plt.savefig(f'{save}.png')
        

        # Apply image preprocessing if required
        # Example 1: Thresholding
        _, thresholded_roi = cv2.threshold(gray_roi, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
        # Example 2: Denoising (using a bilateral filter)
        denoised_roi = cv2.bilateralFilter(thresholded_roi, 9, 75, 75)
    
        # Perform OCR on the preprocessed ROI using pytesseract
        pytesseract.pytesseract.tesseract_cmd = r'YOUR TESSERACT PATH HERE'
        # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        extracted_text = pytesseract.image_to_string(denoised_roi, config='--psm 7')  # Use page segmentation mode 7 for treating the image as a single line of text
        
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
            # print(f"No numbers found in ROI")

        pic = pic + 1
    return a
#Coordinate values to search

image_parts = [{'x1':120, 'y1':0, 'x2':195, 'y2':20},
                {'x1':200, 'y1':0, 'x2':255, 'y2':20},
                {'x1':255, 'y1':0, 'x2':320, 'y2':20},
                {'x1':320, 'y1':0, 'x2':385, 'y2':20},
                {'x1':390, 'y1':0, 'x2':445, 'y2':20},
                {'x1':450, 'y1':0, 'x2':520, 'y2':20},
                {'x1':520, 'y1':0, 'x2':580, 'y2':20},
                {'x1':580, 'y1':0, 'x2':630, 'y2':20},

                {'x1':120, 'y1':20, 'x2':195, 'y2':40},
                {'x1':200, 'y1':20, 'x2':255, 'y2':40},
                {'x1':255, 'y1':20, 'x2':320, 'y2':40},
                {'x1':320, 'y1':20, 'x2':385, 'y2':40},
                {'x1':390, 'y1':20, 'x2':445, 'y2':40},
                {'x1':450, 'y1':20, 'x2':520, 'y2':40},
                {'x1':520, 'y1':20, 'x2':580, 'y2':40},
                {'x1':580, 'y1':20, 'x2':630, 'y2':40},

                {'x1':120, 'y1':40, 'x2':195, 'y2':60},
                {'x1':200, 'y1':40, 'x2':255, 'y2':60},
                {'x1':255, 'y1':40, 'x2':320, 'y2':60},
                {'x1':320, 'y1':40, 'x2':385, 'y2':60},
                {'x1':390, 'y1':40, 'x2':445, 'y2':60},
                {'x1':450, 'y1':40, 'x2':520, 'y2':60},
                {'x1':520, 'y1':40, 'x2':580, 'y2':60},
                {'x1':580, 'y1':40, 'x2':630, 'y2':60},

                {'x1':120, 'y1':60, 'x2':195, 'y2':80},
                {'x1':200, 'y1':60, 'x2':255, 'y2':80},
                {'x1':255, 'y1':60, 'x2':320, 'y2':80},
                {'x1':320, 'y1':60, 'x2':385, 'y2':80},
                {'x1':390, 'y1':60, 'x2':445, 'y2':80},
                {'x1':450, 'y1':60, 'x2':520, 'y2':80},
                {'x1':520, 'y1':60, 'x2':580, 'y2':80},
                {'x1':580, 'y1':60, 'x2':630, 'y2':80},

                {'x1':120, 'y1':80, 'x2':195, 'y2':100},
                {'x1':200, 'y1':80, 'x2':255, 'y2':100},
                {'x1':255, 'y1':80, 'x2':320, 'y2':100},
                {'x1':320, 'y1':80, 'x2':385, 'y2':100},
                {'x1':390, 'y1':80, 'x2':445, 'y2':100},
                {'x1':450, 'y1':80, 'x2':520, 'y2':100},
                {'x1':520, 'y1':80, 'x2':580, 'y2':100},
                {'x1':580, 'y1':80, 'x2':630, 'y2':100},

                {'x1':120, 'y1':100, 'x2':195, 'y2':120},
                {'x1':200, 'y1':100, 'x2':255, 'y2':120},
                {'x1':255, 'y1':100, 'x2':320, 'y2':120},
                {'x1':320, 'y1':100, 'x2':385, 'y2':120},
                {'x1':390, 'y1':100, 'x2':445, 'y2':120},
                {'x1':450, 'y1':100, 'x2':520, 'y2':120},
                {'x1':520, 'y1':100, 'x2':580, 'y2':120},
                {'x1':580, 'y1':100, 'x2':630, 'y2':120},

                {'x1':120, 'y1':120, 'x2':195, 'y2':140},
                {'x1':200, 'y1':120, 'x2':255, 'y2':140},
                {'x1':255, 'y1':120, 'x2':320, 'y2':140},
                {'x1':320, 'y1':120, 'x2':385, 'y2':140},
                {'x1':390, 'y1':120, 'x2':445, 'y2':140},
                {'x1':450, 'y1':120, 'x2':520, 'y2':140},
                {'x1':520, 'y1':120, 'x2':580, 'y2':140},
                {'x1':580, 'y1':120, 'x2':630, 'y2':140},

                {'x1':120, 'y1':140, 'x2':195, 'y2':160},
                {'x1':200, 'y1':140, 'x2':255, 'y2':160},
                {'x1':255, 'y1':140, 'x2':320, 'y2':160},
                {'x1':320, 'y1':140, 'x2':385, 'y2':160},
                {'x1':390, 'y1':140, 'x2':445, 'y2':160},
                {'x1':450, 'y1':140, 'x2':520, 'y2':160},
                {'x1':520, 'y1':140, 'x2':580, 'y2':160},
                {'x1':580, 'y1':140, 'x2':630, 'y2':160},

                {'x1':120, 'y1':160, 'x2':195, 'y2':180},
                {'x1':200, 'y1':160, 'x2':255, 'y2':180},
                {'x1':255, 'y1':160, 'x2':320, 'y2':180},
                {'x1':320, 'y1':160, 'x2':385, 'y2':180},
                {'x1':390, 'y1':160, 'x2':445, 'y2':180},
                {'x1':450, 'y1':160, 'x2':520, 'y2':180},
                {'x1':520, 'y1':160, 'x2':580, 'y2':180},
                {'x1':580, 'y1':160, 'x2':630, 'y2':180},

                {'x1':120, 'y1':180, 'x2':195, 'y2':200},
                {'x1':200, 'y1':180, 'x2':255, 'y2':200},
                {'x1':255, 'y1':180, 'x2':320, 'y2':200},
                {'x1':320, 'y1':180, 'x2':385, 'y2':200},
                {'x1':390, 'y1':180, 'x2':445, 'y2':200},
                {'x1':450, 'y1':180, 'x2':520, 'y2':200},
                {'x1':520, 'y1':180, 'x2':580, 'y2':200},
                {'x1':580, 'y1':180, 'x2':630, 'y2':200},

                {'x1':120, 'y1':200, 'x2':195, 'y2':220},
                {'x1':200, 'y1':200, 'x2':255, 'y2':220},
                {'x1':255, 'y1':200, 'x2':320, 'y2':220},
                {'x1':320, 'y1':200, 'x2':385, 'y2':220},
                {'x1':390, 'y1':200, 'x2':445, 'y2':220},
                {'x1':450, 'y1':200, 'x2':520, 'y2':220},
                {'x1':520, 'y1':200, 'x2':580, 'y2':220},
                {'x1':580, 'y1':200, 'x2':630, 'y2':220},

                {'x1':120, 'y1':220, 'x2':195, 'y2':240},
                {'x1':200, 'y1':220, 'x2':255, 'y2':240},
                {'x1':255, 'y1':220, 'x2':320, 'y2':240},
                {'x1':320, 'y1':220, 'x2':385, 'y2':240},
                {'x1':390, 'y1':220, 'x2':445, 'y2':240},
                {'x1':450, 'y1':220, 'x2':520, 'y2':240},
                {'x1':520, 'y1':220, 'x2':580, 'y2':240},
                {'x1':580, 'y1':220, 'x2':630, 'y2':240},

                {'x1':120, 'y1':240, 'x2':195, 'y2':260},
                {'x1':200, 'y1':240, 'x2':255, 'y2':260},
                {'x1':255, 'y1':240, 'x2':320, 'y2':260},
                {'x1':320, 'y1':240, 'x2':385, 'y2':260},
                {'x1':390, 'y1':240, 'x2':445, 'y2':260},
                {'x1':450, 'y1':240, 'x2':520, 'y2':260},
                {'x1':520, 'y1':240, 'x2':580, 'y2':260},
                {'x1':580, 'y1':240, 'x2':630, 'y2':260},

                {'x1':120, 'y1':260, 'x2':195, 'y2':280},
                {'x1':200, 'y1':260, 'x2':255, 'y2':280},
                {'x1':255, 'y1':260, 'x2':320, 'y2':280},
                {'x1':320, 'y1':260, 'x2':385, 'y2':280},
                {'x1':390, 'y1':260, 'x2':445, 'y2':280},
                {'x1':450, 'y1':260, 'x2':520, 'y2':280},
                {'x1':520, 'y1':260, 'x2':580, 'y2':280},
                {'x1':580, 'y1':260, 'x2':630, 'y2':280},

                {'x1':120, 'y1':280, 'x2':195, 'y2':300},
                {'x1':200, 'y1':280, 'x2':255, 'y2':300},
                {'x1':255, 'y1':280, 'x2':320, 'y2':300},
                {'x1':320, 'y1':280, 'x2':385, 'y2':300},
                {'x1':390, 'y1':280, 'x2':445, 'y2':300},
                {'x1':450, 'y1':280, 'x2':520, 'y2':300},
                {'x1':520, 'y1':280, 'x2':580, 'y2':300},
                {'x1':580, 'y1':280, 'x2':630, 'y2':300},

                {'x1':120, 'y1':300, 'x2':195, 'y2':320},
                {'x1':200, 'y1':300, 'x2':255, 'y2':320},
                {'x1':255, 'y1':300, 'x2':320, 'y2':320},
                {'x1':320, 'y1':300, 'x2':385, 'y2':320},
                {'x1':390, 'y1':300, 'x2':445, 'y2':320},
                {'x1':450, 'y1':300, 'x2':520, 'y2':320},
                {'x1':520, 'y1':300, 'x2':580, 'y2':320},
                {'x1':580, 'y1':300, 'x2':630, 'y2':320},

                {'x1':120, 'y1':320, 'x2':195, 'y2':340},
                {'x1':200, 'y1':320, 'x2':255, 'y2':340},
                {'x1':255, 'y1':320, 'x2':320, 'y2':340},
                {'x1':320, 'y1':320, 'x2':385, 'y2':340},
                {'x1':390, 'y1':320, 'x2':445, 'y2':340},
                {'x1':450, 'y1':320, 'x2':520, 'y2':340},
                {'x1':520, 'y1':320, 'x2':580, 'y2':340},
                {'x1':580, 'y1':320, 'x2':630, 'y2':340},

                {'x1':120, 'y1':340, 'x2':195, 'y2':360},
                {'x1':200, 'y1':340, 'x2':255, 'y2':360},
                {'x1':255, 'y1':340, 'x2':320, 'y2':360},
                {'x1':320, 'y1':340, 'x2':385, 'y2':360},
                {'x1':390, 'y1':340, 'x2':445, 'y2':360},
                {'x1':450, 'y1':340, 'x2':520, 'y2':360},
                {'x1':520, 'y1':340, 'x2':580, 'y2':360},
                {'x1':580, 'y1':340, 'x2':630, 'y2':360},

                {'x1':120, 'y1':360, 'x2':195, 'y2':380},
                {'x1':200, 'y1':360, 'x2':255, 'y2':380},
                {'x1':255, 'y1':360, 'x2':320, 'y2':380},
                {'x1':320, 'y1':360, 'x2':385, 'y2':380},
                {'x1':390, 'y1':360, 'x2':445, 'y2':380},
                {'x1':450, 'y1':360, 'x2':520, 'y2':380},
                {'x1':520, 'y1':360, 'x2':580, 'y2':380},
                {'x1':580, 'y1':360, 'x2':630, 'y2':380},

                {'x1':120, 'y1':380, 'x2':195, 'y2':400},
                {'x1':200, 'y1':380, 'x2':255, 'y2':400},
                {'x1':255, 'y1':380, 'x2':320, 'y2':400},
                {'x1':320, 'y1':380, 'x2':385, 'y2':400},
                {'x1':390, 'y1':380, 'x2':445, 'y2':400},
                {'x1':450, 'y1':380, 'x2':520, 'y2':400},
                {'x1':520, 'y1':380, 'x2':580, 'y2':400},
                {'x1':580, 'y1':380, 'x2':630, 'y2':400},

                {'x1':120, 'y1':400, 'x2':195, 'y2':420},
                {'x1':200, 'y1':400, 'x2':255, 'y2':420},
                {'x1':255, 'y1':400, 'x2':320, 'y2':420},
                {'x1':320, 'y1':400, 'x2':385, 'y2':420},
                {'x1':390, 'y1':400, 'x2':445, 'y2':420},
                {'x1':450, 'y1':400, 'x2':520, 'y2':420},
                {'x1':520, 'y1':400, 'x2':580, 'y2':420},
                {'x1':580, 'y1':400, 'x2':630, 'y2':420},

                {'x1':120, 'y1':420, 'x2':195, 'y2':440},
                {'x1':200, 'y1':420, 'x2':255, 'y2':440},
                {'x1':255, 'y1':420, 'x2':320, 'y2':440},
                {'x1':320, 'y1':420, 'x2':385, 'y2':440},
                {'x1':390, 'y1':420, 'x2':445, 'y2':440},
                {'x1':450, 'y1':420, 'x2':520, 'y2':440},
                {'x1':520, 'y1':420, 'x2':580, 'y2':440},
                {'x1':580, 'y1':420, 'x2':630, 'y2':440},

                {'x1':120, 'y1':440, 'x2':195, 'y2':460},
                {'x1':200, 'y1':440, 'x2':255, 'y2':460},
                {'x1':255, 'y1':440, 'x2':320, 'y2':460},
                {'x1':320, 'y1':440, 'x2':385, 'y2':460},
                {'x1':390, 'y1':440, 'x2':445, 'y2':460},
                {'x1':450, 'y1':440, 'x2':520, 'y2':460},
                {'x1':520, 'y1':440, 'x2':580, 'y2':460},
                {'x1':580, 'y1':440, 'x2':630, 'y2':460},

                {'x1':120, 'y1':460, 'x2':195, 'y2':480},
                {'x1':200, 'y1':460, 'x2':255, 'y2':480},
                {'x1':255, 'y1':460, 'x2':320, 'y2':480},
                {'x1':320, 'y1':460, 'x2':385, 'y2':480},
                {'x1':390, 'y1':460, 'x2':445, 'y2':480},
                {'x1':450, 'y1':460, 'x2':520, 'y2':480},
                {'x1':520, 'y1':460, 'x2':580, 'y2':480},
                {'x1':580, 'y1':460, 'x2':630, 'y2':480},

                {'x1':120, 'y1':480, 'x2':195, 'y2':500},
                {'x1':200, 'y1':480, 'x2':255, 'y2':500},
                {'x1':255, 'y1':480, 'x2':320, 'y2':500},
                {'x1':320, 'y1':480, 'x2':385, 'y2':500},
                {'x1':390, 'y1':480, 'x2':445, 'y2':500},
                {'x1':450, 'y1':480, 'x2':520, 'y2':500},
                {'x1':520, 'y1':480, 'x2':580, 'y2':500},
                {'x1':580, 'y1':480, 'x2':630, 'y2':500},
                
                {'x1':120, 'y1':500, 'x2':195, 'y2':520},
                {'x1':200, 'y1':500, 'x2':255, 'y2':520},
                {'x1':255, 'y1':500, 'x2':320, 'y2':520},
                {'x1':320, 'y1':500, 'x2':385, 'y2':520},
                {'x1':390, 'y1':500, 'x2':445, 'y2':520},
                {'x1':450, 'y1':500, 'x2':520, 'y2':520},
                {'x1':520, 'y1':500, 'x2':580, 'y2':520},
                {'x1':580, 'y1':500, 'x2':630, 'y2':520},
                
                {'x1':120, 'y1':520, 'x2':195, 'y2':540},
                {'x1':200, 'y1':520, 'x2':255, 'y2':540},
                {'x1':255, 'y1':520, 'x2':320, 'y2':540},
                {'x1':320, 'y1':520, 'x2':385, 'y2':540},
                {'x1':390, 'y1':520, 'x2':445, 'y2':540},
                {'x1':450, 'y1':520, 'x2':520, 'y2':540},
                {'x1':520, 'y1':520, 'x2':580, 'y2':540},
                {'x1':580, 'y1':520, 'x2':630, 'y2':540},
                
                {'x1':120, 'y1':540, 'x2':195, 'y2':560},
                {'x1':200, 'y1':540, 'x2':255, 'y2':560},
                {'x1':255, 'y1':540, 'x2':320, 'y2':560},
                {'x1':320, 'y1':540, 'x2':385, 'y2':560},
                {'x1':390, 'y1':540, 'x2':445, 'y2':560},
                {'x1':450, 'y1':540, 'x2':520, 'y2':560},
                {'x1':520, 'y1':540, 'x2':580, 'y2':560},
                {'x1':580, 'y1':540, 'x2':630, 'y2':560},
                
                {'x1':120, 'y1':560, 'x2':195, 'y2':580},
                {'x1':200, 'y1':560, 'x2':255, 'y2':580},
                {'x1':255, 'y1':560, 'x2':320, 'y2':580},
                {'x1':320, 'y1':560, 'x2':385, 'y2':580},
                {'x1':390, 'y1':560, 'x2':445, 'y2':580},
                {'x1':450, 'y1':560, 'x2':520, 'y2':580},
                {'x1':520, 'y1':560, 'x2':580, 'y2':580},
                {'x1':580, 'y1':560, 'x2':630, 'y2':580},
                
                {'x1':120, 'y1':580, 'x2':195, 'y2':600},
                {'x1':200, 'y1':580, 'x2':255, 'y2':600},
                {'x1':255, 'y1':580, 'x2':320, 'y2':600},
                {'x1':320, 'y1':580, 'x2':385, 'y2':600},
                {'x1':390, 'y1':580, 'x2':445, 'y2':600},
                {'x1':450, 'y1':580, 'x2':520, 'y2':600},
                {'x1':520, 'y1':580, 'x2':580, 'y2':600},
                {'x1':580, 'y1':580, 'x2':630, 'y2':600}]



# Define the regions of interest (ROIs) where you want to extract data
def readImage():
    for coordinate in image_parts:
        x1, y1, x2, y2 = coordinate.values()
        roi_coordinates = [
            (x1, y1, x2, y2),  # Format: (top-left x, top-left y, bottom-right x, bottom-right y)
        ]
        read_character(roi_coordinates)

s = 1
while s == 1:
    start_time = time.time()
    print(datetime.now())
    ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

    region = (26, 248, 640, 700)
    im = pyscreeze.screenshot('tos.png', region)

    readImage()
    # print(a)

    x = a[0] + " " + a[1] + " " + a[2] + " " + a[3] + " " + a[4] + " " + a[5] + " " + a[6] + " " + a[7]
    y = a[8] + " " + a[9] + " " + a[10] + " " + a[11] + " " + a[12] + " " + a[13] + " " + a[14] + " " + a[15]
    z = a[16] + " " + a[17] + " " + a[18] + " " + a[19] + " " + a[20] + " " + a[21] + " " + a[22] + " " + a[23]
    t = a[24] + " " + a[25] + " " + a[26] + " " + a[27] + " " + a[28] + " " + a[29] + " " + a[30] + " " + a[31]
    u = a[32] + " " + a[33] + " " + a[34] + " " + a[35] + " " + a[36] + " " + a[37] + " " + a[38] + " " + a[39]

    v = a[40] + " " + a[41] + " " + a[42] + " " + a[43] + " " + a[44] + " " + a[45] + " " + a[46] + " " + a[47]
    w = a[48] + " " + a[49] + " " + a[50] + " " + a[51] + " " + a[52] + " " + a[53] + " " + a[54] + " " + a[55]
    x1 = a[56] + " " + a[57] + " " + a[58] + " " + a[59] + " " + a[60] + " " + a[61] + " " + a[62] + " " + a[63]
    y1 = a[64] + " " + a[65] + " " + a[66] + " " + a[67] + " " + a[68] + " " + a[69] + " " + a[70] + " " + a[71]
    z1 = a[72] + " " + a[73] + " " + a[74] + " " + a[75] + " " + a[76] + " " + a[77] + " " + a[78] + " " + a[79]

    t1 = a[80] + " " + a[81] + " " + a[82] + " " + a[83] + " " + a[84] + " " + a[85] + " " + a[86] + " " + a[87]
    u1 = a[88] + " " + a[89] + " " + a[90] + " " + a[91] + " " + a[92] + " " + a[93] + " " + a[94] + " " + a[95]
    v1 = a[96] + " " + a[97] + " " + a[98] + " " + a[99] + " " + a[100] + " " + a[101] + " " + a[102] + " " + a[103]
    w1 = a[104] + " " + a[105] + " " + a[106] + " " + a[107] + " " + a[108] + " " + a[109] + " " + a[110] + " " + a[111]
    x2 = a[112] + " " + a[113] + " " + a[114] + " " + a[115] + " " + a[116] + " " + a[117] + " " + a[118] + " " + a[119]

    y2 = a[120] + " " + a[121] + " " + a[122] + " " + a[123] + " " + a[124] + " " + a[125] + " " + a[126] + " " + a[127]
    z2 = a[128] + " " + a[129] + " " + a[130] + " " + a[131] + " " + a[132] + " " + a[133] + " " + a[134] + " " + a[135]
    t2 = a[136] + " " + a[137] + " " + a[138] + " " + a[139] + " " + a[140] + " " + a[141] + " " + a[142] + " " + a[143]
    u2 = a[144] + " " + a[145] + " " + a[146] + " " + a[147] + " " + a[148] + " " + a[149] + " " + a[150] + " " + a[151]
    v2 = a[152] + " " + a[153] + " " + a[154] + " " + a[155] + " " + a[156] + " " + a[157] + " " + a[158] + " " + a[159]

    w2 = a[160] + " " + a[161] + " " + a[162] + " " + a[163] + " " + a[164] + " " + a[165] + " " + a[166] + " " + a[167]
    x3 = a[168] + " " + a[169] + " " + a[170] + " " + a[171] + " " + a[172] + " " + a[173] + " " + a[174] + " " + a[175]
    y3 = a[176] + " " + a[177] + " " + a[178] + " " + a[179] + " " + a[180] + " " + a[181] + " " + a[182] + " " + a[183]
    z3 = a[184] + " " + a[185] + " " + a[186] + " " + a[187] + " " + a[188] + " " + a[189] + " " + a[190] + " " + a[191]
    t3 = a[192] + " " + a[193] + " " + a[194] + " " + a[195] + " " + a[196] + " " + a[197] + " " + a[198] + " " + a[199]

    u3 = a[200] + " " + a[201] + " " + a[202] + " " + a[203] + " " + a[204] + " " + a[205] + " " + a[206] + " " + a[207]
    v3 = a[208] + " " + a[209] + " " + a[210] + " " + a[211] + " " + a[212] + " " + a[213] + " " + a[214] + " " + a[215]
    w3 = a[216] + " " + a[217] + " " + a[218] + " " + a[219] + " " + a[220] + " " + a[221] + " " + a[222] + " " + a[223]
    x4 = a[224] + " " + a[225] + " " + a[226] + " " + a[227] + " " + a[228] + " " + a[229] + " " + a[230] + " " + a[231]
    y4 = a[232] + " " + a[233] + " " + a[234] + " " + a[235] + " " + a[236] + " " + a[237] + " " + a[238] + " " + a[239]






    # print(x)
    # print(y)
    # print(z)
    # print(t)
    # print(u)

    # print("------------------------------------")

    # print(v)
    # print(w)
    # print(x1)
    # print(y1)
    # print(z1)

    # print("------------------------------------")

    # print(t1)
    # print(u1)
    # print(v1)
    # print(w1)
    # print(x2)

    # print("------------------------------------")

    # print(y2)
    # print(z2)
    # print(t2)
    # print(u2)
    # print(v2)

    # print("------------------------------------")

    # print(w2)
    # print(x3)
    # print(y3)
    # print(z3)
    # print(t3)

    write1(x = x)
    write2(x = y)
    write3(x = z)
    write4(x = t)
    write5(x = u)

    write6(x = v)
    write7(x = u)
    write8(x = x1)
    write9(x = y1)
    write10(x = z1)

    write11(x = t1)
    write12(x = u1)
    write13(x = v1)
    write14(x = w1)
    write15(x = x2)

    write16(x = y2)
    write17(x = z2)
    write18(x = t2)
    write19(x = u2)
    write20(x = v2)

    write21(x = w2)
    write22(x = x3)
    write23(x = y3)
    write24(x = z3)
    write25(x = t3)

    write26(x = u3)
    write27(x = v3)
    write28(x = w3)
    write29(x = x4)
    write30(x = y4)


    # print(x)
    # print(y)
    # print(z)
    # print(t)
    # print(u)



    end_time = time.time()
    total_time = end_time - start_time

    print(total_time)
    tsleep = 180 - total_time

    # print(tsleep)
    time.sleep(tsleep)
    # print(datetime.now())
    a = []


