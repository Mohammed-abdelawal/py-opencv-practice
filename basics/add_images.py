from cv2 import cv2

img_mask = cv2.imread('data/anon.png')

img_me = cv2.imread('data/me.jpg')

rows,cols,channels = img_mask.shape

roi = img_me[0:rows, 0:cols ]


img_mask_gray = cv2.cvtColor(img_mask,cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img_mask_gray, 250, 255, cv2.THRESH_BINARY)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

img2_fg = cv2.bitwise_and(img_mask,img_mask,mask = mask)

dst = cv2.add(img1_bg,img2_fg)

img_me[0:rows, 0:cols ] = dst

cv2.imshow('res',img_me)

cv2.waitKey(0)
cv2.destroyAllWindows()
