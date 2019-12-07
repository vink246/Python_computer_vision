import time
import cv2
import mss
import numpy as np
import keyboard
import pytesseract
f = 0
t = 0
lef = 720
with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {'top': 280, 'left': 710, 'width': 100, 'height': 70}
    c ={'top': 275, 'left': 940, 'width': 12, 'height': 12}

    while 'Screen capturing':
        monitor = {'top': 280, 'left': lef, 'width': 100, 'height': 70}
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = np.array(sct.grab(monitor))
        st = np.array(sct.grab(c))
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        frame3 = cv2.cvtColor(st, cv2.COLOR_BGR2GRAY)

        start = frame3[1,1]
        if start < 100:
            print('start')
            keyboard.press('space')
            time.sleep(0.2)
            keyboard.release('space')
            t = 0
            lef = 720
        else:
            val = frame3[10,10]
            for i in range(1,30):
                check = frame[45,20+i]
                check2 = frame[25,20+i]
                if check < 100 or check2 < 100:
                    t = t+1
                    if t>20:
                        lef = 770
                    if t>40:
                        lef = 800
                    keyboard.press('space')
                    time.sleep(0.4)
                    keyboard.release('space')
                    keyboard.press('down_arrow')
                    time.sleep(0.1)
                    keyboard.release('down_arrow')
                    break
