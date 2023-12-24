import cv2 as c
import numpy as np

# cv2.copyMakeBorder() function used to create border
# it take parameters like (img, border width(4sides),border type, value in bgr color)

img = c.imread("D:\\OpenCV\\images\\img2.jpg")

img = c.resize(img,(500,600))

brdr = c.copyMakeBorder(img,10,10,5,5,c.BORDER_CONSTANT,value=(0,0,255))

c.imshow('org wind',brdr)
c.waitKey(0)
c.destroyAllWindows()