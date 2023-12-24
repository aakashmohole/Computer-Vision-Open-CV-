#Threholding is a segmentation techique which is use to separate selected object from an image.

#Image Thresholding -  If pixel value is greater than a threshold value
#it is assigned one value (may be white), 
#else it is assigned another value (may be black).
#thresholding is use to subtract image from background
#Thresholding is of  3 type -  Simple thresholding, Adaptive thresholding, Otsu’s thresholding
#image should be in gray scale
#simple thresholding(img,pixel_thresh,_max_thresh_pixel,style)
#it return 2 values - one is random data , second is threshold

import cv2
import numpy as np
from matplotlib import pyplot as plt

# def nothing():
#     pass

# cv2.namedWindow('adj')
# cv2.createTrackbar('threshold_val','adj',0,255,nothing)

img = cv2.imread('D:\\OpenCV\\Images\\img7.jpg')
img = cv2.resize(img,(400,500))
img_gry = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# a = cv2.getTrackbarPos('threshold_val','adj')

_,img_thr1 = cv2.threshold(img_gry,20,150,cv2.THRESH_BINARY)
_,img_thr2 = cv2.threshold(img_gry,30,100,cv2.THRESH_BINARY_INV)
_,img_thr3 = cv2.threshold(img_gry,40,180,cv2.THRESH_TRUNC)
_,img_thr4 = cv2.threshold(img_gry,50,155,cv2.THRESH_TOZERO)
_,img_thr5 = cv2.threshold(img_gry,20,155,cv2.THRESH_TOZERO_INV)


# matplot library used to disply all imges in singl fram and anylise data
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, img_thr1 ,img_thr2 ,img_thr3 ,img_thr4, img_thr5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()

# cv2.imshow('org',img)
# cv2.imshow('gry',img_gry)
# cv2.imshow('thr1',img_thr1)
# cv2.imshow('thr2',img_thr2)
# cv2.imshow('thr3',img_thr3)
# cv2.imshow('thr4',img_thr4)
# cv2.imshow('thr5',img_thr5)
# cv2.waitKey(0)
# cv2.destroyAllWindows()










