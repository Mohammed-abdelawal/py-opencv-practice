from cv2 import cv2
import numpy as np 

img = cv2.imread('data/home.png')

print(img.item(100,100,0))

print(img.shape)

print(img.size)

print(img.dtype)

ball = img[280:340, 330:390]

cv2.imshow('old',img)
cv2.imshow('cropped area',ball)

img[273:333, 100:160] = ball
cv2.imshow('new',img)


cv2.waitKey(0)
cv2.destroyAllWindows()
