import cv2
img1=cv2.imread('star.jpg')
img2=cv2.imread('dot.jpg')
subtractedimage=cv2.subtract(img1,img2)
cv2.imshow('subtractimg',subtractedimage)
cv2.waitKey(0)