import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread("img1.jpg")
col_in_img=('r','b','g')
for key,value in enumerate(col_in_img):
    histogm=cv.calcHist([img],[key],None,[256],[0,256])
    plt.plot(histogm,color=value)
    plt.xlim([0,256])
plt.show()
"""
while True:
    cv.imshow('project2',img)
    if cv.waitKey(1)==ord('q'):
        break
cv.destroyAllWindows()
"""