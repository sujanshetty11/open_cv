import cv2
import matplotlib.pyplot as plt
img=cv2.imread("sujan1.jpg")
re=cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)
cv2.imshow("resized",re)

# gray= cv2.cvtColor(re,cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray",gray)
# gray_hist=cv2.calcHist([gray],[0],None,[256],[0,256])
# plt.figure()
# plt.title('grayscale histogram')
# plt.xlabel('bins')
# plt.ylabel("# of pixels")
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

#color histogram
colors=('b','g','r')
for i , col in enumerate(colors):
    hist=cv2.calcHist([re],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])


plt.show()


cv2.waitKey(0)