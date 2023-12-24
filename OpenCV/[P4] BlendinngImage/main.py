"""
blinding img with openCV
here we use 2 fun cv2.add() and cv2.addWight()
blinding means addition of two images
we need both images in same size
"""

import cv2
import numpy as np

img1 = cv2.imread("D:\\OpenCV\\images\\Goku.jpg")
img1 = cv2.resize(img1,(500,600))
img2 = cv2.imread("D:\\OpenCV\\images\\img1.jpg")
img2 = cv2.resize(img2,(500,600))

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

# firset add() function addition in numpy
# res = img1+img2
# cv2.imshow('res',res)

#inbult add() functon of openCV
# res = cv2.add(img1,img2)
# cv2.imshow('res',res)

# recomanded to use addWight() function
# sum of both weight of imgaes is maximum 1
# addWeighte(img1,wt1,img2,wt2,gama_val)
res = cv2.addWeighted(img1,0.7,img2,0.3,0)
cv2.imshow('res',res)

cv2.waitKey(0)
cv2.destroyAllWindows()