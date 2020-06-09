from cv2 import cv2

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)
print('CV2 Have ',len(flags),'Color Spaces') # 274 in mine
