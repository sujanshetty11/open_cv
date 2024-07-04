import cv2
import numpy as np
img= cv2.imread('sujan1.jpg')
re= cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)
cv2.imshow("image1",re)

gray=cv2.cvtColor(re,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

lap= cv2.Laplacian(gray, cv2.CV_64F )
lap=np.uint8(np.absolute(lap))
cv2.imshow('laplacian',lap)

#sobel
sobelx=cv2.Sobel(gray,cv2.CV_64F,1,0)
sobely=cv2.Sobel(gray,cv2.CV_64F,0,1)
combined=cv2.bitwise_or(sobelx,sobely)
cv2.imshow("sobelx",sobelx)
cv2.imshow('sobely',sobely)
cv2.imshow('combined',combined)
cv2.waitKey(0)