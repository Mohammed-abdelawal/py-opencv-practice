from cv2 import cv2

image = cv2.imread('data/home.png')
cv2.imshow("image",image)
cv2.waitKey(0)

cv2.destroyAllWindows()