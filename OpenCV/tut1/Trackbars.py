import cv2
import numpy as np
cap = cv2.VideoCapture(0)
def nothing(x):
    pass
cv2.namedWindow("Trackbar")
cv2.createTrackbar("L-H","Trackbar",0,179,nothing)
cv2.createTrackbar("L-S","Trackbar",149,255,nothing)
cv2.createTrackbar("L-V","Trackbar",149,255,nothing)
cv2.createTrackbar("U-H","Trackbar",2,179,nothing)
cv2.createTrackbar("U-S","Trackbar",255,255,nothing)
cv2.createTrackbar("U-V","Trackbar",255,255,nothing)

cv2.createTrackbar("Threshold-1","Trackbar",0,1000,nothing)
cv2.createTrackbar("Threshold-2","Trackbar",0,1000,nothing)
while True:
    ret, frame = cap.read()
    l_h = cv2.getTrackbarPos("L-H","Trackbar")
    l_s = cv2.getTrackbarPos("L-S","Trackbar")
    l_v = cv2.getTrackbarPos("L-V","Trackbar")
    u_h = cv2.getTrackbarPos("U-H","Trackbar")
    u_s = cv2.getTrackbarPos("U-S","Trackbar")
    u_v = cv2.getTrackbarPos("U-V","Trackbar")
    Threshold1 = cv2.getTrackbarPos("Threshold-1","Trackbar")
    Threshold2 = cv2.getTrackbarPos("Threshold-2","Trackbar")
    lower_range = np.array([l_h,l_s,l_v])
    higher_range = np.array([u_h, u_s, u_v])




    cv2.imshow('Frame3', frame)

    blurred_frame = cv2.GaussianBlur(frame,(5,5),0)
    kernel = np.ones((3,3),np.uint8)
    hsv = cv2.cvtColor(blurred_frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_range, higher_range)
    mask = cv2.medianBlur(mask,3)
    mask = cv2.dilate(mask,kernel,3)
    contoure, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    result = cv2.bitwise_and(frame, frame, mask=mask)
    canny = cv2.Canny(result,Threshold1,Threshold2)

    cv2.imshow('edge', canny)


    for c in contoure:
        area = cv2.contourArea(c)
        if area>1000:
            cv2.drawContours(result, contoure, -1, (0, 255, 0), 3)
    cv2.imshow('Frame1', result)

    cv2.imshow('Frame2', mask)
    cv2.imshow('Frame1', result)
    if cv2.waitKey(1) == ord('q'):
        break

framespersecond= int(cap.get(cv2.CAP_PROP_FPS))

print("The total number of frames in this video is ", framespersecond)

cap.release()
cv2.destroyAllWindows()