import cv2
import numpy as np
img=cv2.imread('pic3.jpg')
cv2.imshow("image1",img)

blank=np.zeros(img.shape,dtype="uint8")
cv2.imshow("blank",blank)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gary",gray)

# blur=cv2.GaussianBlur(gray,(5,5),cv2.BORDER_DEFAULT)
# cv2.imshow("blur",blur)

# canny=cv2.Canny(img,125,175)
# cv2.imshow("canny",canny)

ret,thresh=cv2.threshold(gray,125,225,cv2.THRESH_BINARY)
cv2.imshow("thresh",thresh)
contours,heirarchies=cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')
cv2.drawContours(blank,contours,-1,(0,0,225),1)
cv2.imshow('contours drawn',blank)




cv2.waitKey(0)