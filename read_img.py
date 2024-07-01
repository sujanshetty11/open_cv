import cv2 
# reading image
Img=cv2.imread('photos/pic1.jpg')
cv2.imshow('pic1', Img) 

cv2.waitKey(0)
cv2.destroyAllWindows()

# reading vdo
# capture=cv2.VideoCapture('vdo.mp4')
# while True :
#     isTrue, frame=capture.read()
#     cv2.imshow('Video',frame)

#     if cv2.waitKey(20)& 0xFF==ord('d'):
#         break

# capture.release()
# cv2.destroyAllWindows()





