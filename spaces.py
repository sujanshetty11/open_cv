import cv2
import numpy as np
import matplotlib.pyplot as plt


img=cv2.imread('sujan1.jpg')
re=cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)
cv2.imshow("sujan",re)
# bgr to gray,hsv and lab 
# gray=cv2.cvtColor(re,cv2.COLOR_BGR2GRAY)# change color_bgr2xyz , xyz could be hsv lab or gray 
# cv2.imshow("gray",gray)

# def translate(re,x,y):
#     transMat=np.float32([[1,0,x],[0,1,y]])
#     dimensions=(re.shape[1],re.shape[0])
#     return cv2.warpAffine(re,transMat,dimensions)

# translated=translate(re,100,100)
# cv2.imshow("translated",translated)
''' you cannot convert gary image to hsv directly
instead convert first to bgr then to hsv'''
plt.imshow(re)
plt.show()





cv2.waitKey(0)
cv2.destroyAllWindows()