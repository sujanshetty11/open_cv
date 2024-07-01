import cv2 
# reading image
# Img=cv2.imread('photos/pic1.jpg')
# cv2.imshow('pic1', Img) 

def rescaleframe(frame,scale=0.75):
    width=int(frame.shape[1] * scale)
    height=int(frame.shape[1] * scale)
    dimensions=(width,height)

    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)

 #reading vdo

capture=cv2.VideoCapture('vdo.mp4')
while True :
    isTrue, frame=capture.read()

    frame_resized = rescaleframe(frame)
    # cv2.imshow('Video',frame)
    cv2.imshow('video resized', frame_resized)

    if cv2.waitKey(20)& 0xFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows()

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# reading vdo
# capture=cv2.VideoCapture('vdo.mp4')
# while True :
#     isTrue, frame=capture.read()
#     cv2.imshow('Video',frame)

#     if cv2.waitKey(20)& 0xFF==ord('d'):
#         break

# capture.release()
# cv2.destroyAllWindows()

