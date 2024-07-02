import cv2
import numpy as np
img=cv2.imread('pic3.jpg')
cv2.imshow('image',img)
#translation

def translate(img,x,y):
    transmat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv2.warpAffine(img,transmat,dimensions)
#-x --> left
#-y --> up
#x --> right
#y --> down 

translated=translate(img,100,100) #shift by 100 through right and down 
cv2.imshow("translated",translated)

#rotation
def rotate (img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv2.getRotationMatrix2D(rotPoint,angle,1.09)
    dimensions=(width,height)
    return cv2.warpAffine(img,rotMat,dimensions)
rotated=rotate(img,45)
cv2.imshow("rotated",rotated)

#flipping

flip=cv2.flip(img,0)#change value 0 to 1,-1 for horizontal and vertical flipping
cv2.imshow("flipped image",flip)




cv2.waitKey(0)