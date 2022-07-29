import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('Frame',hsv)
    lower_range= np.array([141,155,84])
    higher_range = np.array([179,255,255])
    mask = cv2.inRange(hsv,lower_range,higher_range)
    result = cv2.bitwise_and(frame,frame,mask = mask)
    cv2.imshow('Frame1', result)
    if cv2.waitKey(1)== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()