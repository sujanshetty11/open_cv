import cv2
img=cv2.imread("sujan1.jpg")

re= cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)
cv2.imshow("imag1",re)
gray=cv2.cvtColor(re,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

threshold,thresh=cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
cv2.imshow("threshold",thresh)

threshold,thresh_inv=cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)
cv2.imshow("threshold inverse",thresh_inv)

#adaptive thresholding
adaptive_thresh= cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,3)
cv2.imshow("adaptive thresholding",adaptive_thresh)

cv2.waitKey(0)