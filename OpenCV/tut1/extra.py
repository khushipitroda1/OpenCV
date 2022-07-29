import cv2
import numpy as np
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('Frame',hsv)
    lower_range= np.array([141,155,84])
    higher_range = np.array([179,255,255])

    mask = cv2.inRange(hsv,lower_range,higher_range)
    blue = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]

    if len(blue)>0:
        blue_area = max(blue,key=cv2.contourArea)
        (xg,yg,wg,hg)=cv2.boundingRect(blue_area)
        cv2.rectangle(frame,(xg,yg),(xg+wg,yg+hg),(0,255,2),2)
        cv2.putText(frame,"RED OBJECT",(xg,yg-15),font,5,(0,0,0),cv2.LINE_AA)

    result = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('Frame1', result)
    if cv2.waitKey(1)== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()