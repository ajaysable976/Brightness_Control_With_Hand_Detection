# Installed Libraries
import cv2 
import mediapipe as mp
from math import hypot
import screen_brightness_control as sbc
import numpy as np 

cap = cv2.VideoCapture(0)

# 1. drawing_utils used to set up the drawing function of hands landmarks on the image
# 2. MediaPipe Hands is a high-fidelity hand and finger tracking solution. It employs   machine learning (ML) to infer 21 3D landmarks of a hand from just a single frame
# 3. cv2. cvtColor() method is used to convert an image from one color space to another. There are more than 150 color-space conversion methods available in OpenCV
# 4. cap. read() returns a bool ( True / False ). If the frame is read correctly, it will be True . So you can check for the end of the video by checking this returned value.



mpHands = mp.solutions.hands 
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


while True:
    success,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    lmList = []
    if results.multi_hand_landmarks:
            for handlandmark in results.multi_hand_landmarks:
                for id,lm in enumerate(handlandmark.landmark):
                    h,w,_ = img.shape
                    cx,cy = int(lm.x*w),int(lm.y*h)
                    lmList.append([id,cx,cy]) 
                mpDraw.draw_landmarks(img,handlandmark,mpHands.HAND_CONNECTIONS)
    if lmList != []:
        x1,y1 = lmList[4][1],lmList[4][2]
        x2,y2 = lmList[8][1],lmList[8][2]

        cv2.circle(img,(x1,y1),4,(320,0,0),cv2.FILLED)
        cv2.circle(img,(x2,y2),4,(320,0,0),cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(320,0,0),3)

        length = hypot(x2-x1,y2-y1)

        bright = np.interp(length,[15,250],[0,100])
        print(bright,length)
        sbc.set_brightness(int(bright))
        
        # Hand range 15 - 220
        # Brightness range 0 - 100

    cv2.imshow('Image',img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break