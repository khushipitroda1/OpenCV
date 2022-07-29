import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    array = np.zeros((width,width,frame.shape[2]),np.uint8)

    small1 = cv2.resize(frame,(width,width))
    small = cv2.resize(small1,(0,0),fx=0.5,fy=0.5)
    temp = small
    array[:width//2,:width//2]= small
    small = cv2.rotate(temp,cv2.cv2.ROTATE_180)
    array[width//2:,:width//2]=small
    small = cv2.rotate(temp,cv2.cv2.ROTATE_90_CLOCKWISE)

    array[width // 2:, width // 2:] = small
    small = cv2.rotate(temp,cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
    array[:width // 2, width // 2:] = small
    cv2.imshow('frame',array)
    if cv2.waitKey(1 )== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()