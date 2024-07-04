import cv2
import numpy as np
img=cv2.imread("sujan1.jpg")
re=cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)
cv2.imshow("image",re)
blank=np.zeros(re.shape[:2],dtype='uint8')
cv2.imshow('blank',blank)
mask=cv2.circle(blank,(re.shape[1]//2,re.shape[0]//2),100,255,-1)
cv2.imshow("mask",mask)

masked_image=cv2.bitwise_and(re,re,mask=mask)
cv2.imshow("masked image",masked_image)





cv2.waitKey(0)