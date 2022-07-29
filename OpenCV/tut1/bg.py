import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, init_frame = cap.read()
    if(ret):
        cv2.imshow("image",init_frame)
        if cv2.waitKey(5) == ord('q'):
            cv2.imwrite("image.jpg",init_frame)
            break

cap.release()
cv2.destroyAllWindows()
