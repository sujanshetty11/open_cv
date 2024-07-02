import cv2
img=cv2.imread("pic3.jpg")
cv2.imshow("image",img)
#convert image to grayscale

# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("image",gray)

# #blur
# blur=cv2.GaussianBlur(img,(3,3),cv2.BORDER_DEFAULT)
# cv2.imshow("blur",blur)

# #edge cascade

# canny=cv2.Canny(img,125,175)
# cv2.imshow("canny",canny)

# #dilating the image

# dilated=cv2.dilate(canny,(11,11),iterations=1)
# cv2.imshow("dialted",dilated)

# #eroded 
# eroded=cv2.erode(dilated,(3,7),iterations=1)
# cv2.imshow("eroded",eroded)

#resize and crop a image

resized=cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)
cv2.imshow("resized",resized)

cropped=resized[50:200,200:400]
cv2.imshow("cropped",cropped)



cv2.waitKey(0)
