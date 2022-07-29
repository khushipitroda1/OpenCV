import cv2  # for image processing
import numpy as np  # mathematical library for image handling


canvas = np.zeros((500,500,3))


cv2.circle(canvas, (250,250), 200, (255,255,255),2)
cv2.imshow("Hii",canvas)
cv2.waitKey(2000)