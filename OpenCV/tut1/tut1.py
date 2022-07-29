import cv2
import random
img = cv2.imread('assets/hello2.PNG',-1)
img2 = cv2.imread('assets/hello2.PNG',1)

print(type(img))

for i in range(100):
    for j in range(100):
        img[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255),0]
cv2.imshow('Image',img)
#cv2.imshow('Image2',img2)
cv2.waitKey(0)
cv2.destroyAllWindow()