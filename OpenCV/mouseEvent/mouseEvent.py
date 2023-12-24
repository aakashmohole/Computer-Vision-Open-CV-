import cv2
import numpy as np

def draw(event,x,y,flag,param):
    print("x: ",x)
    print("y: ",y)
    print("flag: ",flag)
    print("param: ",param)
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.line(img,(50,70),(150,230),(0,255,255),5)
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.arrowedLine(img,(10,10),(150,200),(0,0,255),10)

# we need to set window name and pass event on that window
cv2.namedWindow(winname= "Live")        

img = np.zeros((512,512,3),np.uint8)

cv2.setMouseCallback("Live",draw)

while True:
    cv2.imshow('Live',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()