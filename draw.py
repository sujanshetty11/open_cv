import cv2
import numpy as np 
blank=np.zeros((500,500,3),dtype='uint8')
cv2.imshow('Blank', blank)

img=cv2.imread("pic3.jpg")
cv2.imshow('pic', img)
#paint the img
blank[200:300,300:400]=0,0,255
cv2.imshow('Green',blank)
# draw a rectangle
cv2.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)
cv2.imshow("rectangle",blank)
#write text 
cv2.putText(blank,"hello it's me sujan ",(0,255),cv2.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=2)
cv2.imshow("image",blank)
cv2.waitKey(0)

