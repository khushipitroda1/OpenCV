import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(grey,100,0.1,10)
    corners = np.int0(corners)

    print(corners)
    for c in corners:
        x,y = c.ravel()
        cv2.circle(frame,(x,y),10,(255,0,0),-1)
    cv2.imshow('Frame1', frame)
    cv2.imshow('Frame2', grey)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
