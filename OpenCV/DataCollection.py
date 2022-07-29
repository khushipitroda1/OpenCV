import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands = 1)
imgSize = 300
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x,y,w,h = hand['bbox']

        imgWhite = np.ones((imgSize,imgSize,3),np.uint8)*255
        imgCrop = img[y-20:y+h+20,x-20:x+w+20]
        aspectRatio = h/w
        if aspectRatio>1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop,(wCal,imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize-wCal)/2)
            imgWhite[:, wGap:wCal+wGap] = imgResize
        cv2.imshow("ImageCrop",imgCrop)
        cv2.imshow("imgWhite", imgWhite)



    cv2.imshow("Image",img)
    cv2.waitKey(1)