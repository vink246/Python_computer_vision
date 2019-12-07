from PIL import Image
import pytesseract
import cv2
import os
import time
import numpy as np

cam = cv2.VideoCapture(0)
time.sleep(3)
ret_val,img = cam.read()
scale_factor = 2.5
img = cv2.resize(img,None,fx=scale_factor, fy=scale_factor, interpolation = cv2.INTER_CUBIC)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_black = np.array([0,0,20])
upper_black = np.array([255,255,100])
mask = cv2.inRange(hsv, lower_black, upper_black)
kernel = np.ones((5,5),np.float32)/20
img = cv2.filter2D(mask,-1,kernel)

img = cv2.bitwise_not(img)
cv2.imshow('my webcam', img)
cv2.imwrite("helping.png", img)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open("helping.png"))
print(text)
print("ok")
