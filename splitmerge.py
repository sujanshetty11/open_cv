import cv2 
import numpy as np

img=cv2.imread("sujan1.jpg")
re=cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)
cv2.imshow("image 1",re)

b,g,r=cv2.split(re)
cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)

print(re.shape)
print(b.shape)
print(g.shape)
print(r.shape)

mergedimg=cv2.merge([b,g,r])
cv2.imshow("merged",mergedimg)


cv2.waitKey(0)
cv2.destroyAllWindows(0)