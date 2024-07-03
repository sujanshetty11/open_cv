import cv2
img=cv2.imread("sujan1.jpg")
re=cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)
cv2.imshow("image",re)

#averaging
average=cv2.blur(re,(3,7))
cv2.imshow("blur",average)

#Gaussian blur
gauss=cv2.GaussianBlur(re,(3,7),0)
cv2.imshow("gaussian",gauss)

#Median blur
med=cv2.medianBlur(re,3)
cv2.imshow("median",med)

#Bilateral blur
bi=cv2.bilateralFilter(re,5,88,77)
cv2.imshow("bilateral",bi)



cv2.waitKey(0)
cv2.destroyAllWindows()