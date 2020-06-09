from cv2 import cv2
import numpy as np

img1 = cv2.imread('data/tree.png')
img2 = cv2.imread('data/me.jpg')

dst = cv2.addWeighted(img1,0.4,img2,0.6,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
