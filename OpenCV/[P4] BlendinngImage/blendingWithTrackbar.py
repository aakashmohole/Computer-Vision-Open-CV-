import cv2
import numpy as np

img1 = cv2.imread("D:\\OpenCV\\images\\Goku.jpg")
img1 = cv2.resize(img1,(500,600))
img2 = cv2.imread("D:\\OpenCV\\images\\img1.jpg")
img2 = cv2.resize(img2,(500,600))
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

def blend():
    pass

img = np.zeros([300,300,3],np.uint8)
cv2.namedWindow('win')
# crete trackbar
cv2.createTrackbar('alpha','win',1,100,blend)
switch = "0. Off\n1. On"
cv2.createTrackbar(switch,'win',0,1,blend)

while True:
    s = cv2.getTrackbarPos(switch,'win')
    a = cv2.getTrackbarPos('alpha','win')
    n = float(a/100)
    print(n)
    
    if s == 0:
        dst = img[:]
    else:
        cv2.imshow('dst',dst)
        dst = cv2.addWeighted(img1,1-n,img2,n,0)
        cv2.putText(dst,str(a),(20,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)
        
    k = cv2.waitKey(1)
    if k == 27:
        break
    
cv2.destroyAllWindows()