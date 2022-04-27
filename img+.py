import cv2
image1 = cv2.imread('img1.jpg')
image2 = cv2.imread('img2.jpg')
addedimages = cv2.addWeighted(image1,0.5,image2,0.5,0)
cv2.imshow('addimg',addedimages)
cv2.waitKey(0)