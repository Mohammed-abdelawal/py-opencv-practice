from cv2 import cv2
import random

#cap = cv2.VideoCapture(0) # for live video from your cam
cap = cv2.VideoCapture('data/v.mp4') # for get video from file


while True:

    ret ,frame = cap.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()