from discord import *
from datetime import datetime


import numpy as np
import cv2

FRAMECT = 25 # amount of frames of a cat being on screen
             # once this is reached we send it to discord.


cat_cascade = cv2.CascadeClassifier(r"./cascade.xml")
cap = cv2.VideoCapture(0) # webcam

wait = 0
cat_frames_count = 0


while 1:
    ret, img = cap.read()
    h,w,d=img.shape

    font = cv2.FONT_HERSHEY_SIMPLEX | cv2.FONT_ITALIC
    cv2.putText(img, str(datetime.now().strftime("%I:%M:%S %p %m/%d/%Y")), (10, h-20),
                font, 1, (255,255,255), 2, cv2.LINE_AA)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cat_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        fileName = f'frames/frame_{cat_frames_count}.jpg'
        print(f"[{datetime.now()}] detected cat. wait now equals {wait}")
        wait += 1
        # 25 frames of a cat. this isn't a false positive.
        # save
        if wait == FRAMECT: # save it
            cv2.imwrite(fileName, img)
            # now send it to discord
            SendToDiscord(fileName)
            cat_frames_count += 1
            wait = 0


    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()