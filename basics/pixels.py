from cv2 import cv2
import numpy as np 
import random

img = cv2.imread('data/home.png')


cv2.imshow('old',img)

b,g,r = cv2.split(img)
img = cv2.merge((b,r,g))

cv2.imshow('new',img)



cap = cv2.VideoCapture(0)
while True:

    c = random.randint(0,255)

    ret ,frame = cap.read()
    
    frame[0:30,0:30] = [c,c,c]

    t = frame[0:30,0:30]

    frame[::30,::30] = [c,c,c]

    cv2.imshow("pixel plays",frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
