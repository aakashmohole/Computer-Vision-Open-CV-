import cv2
import numpy as np

# func to set trackbars in off mode 
def cross(x):
    pass

# create blank window
img = np.zeros((300,500,3),np.uint8)
cv2.namedWindow("Color Picker by Aakash")
#crete track barse
swith = "0:off\n1:on"

# here track bar tekae 5 par (str,windname,first ni to last no,fun)
cv2.createTrackbar(swith,"Color Picker by Aakash",0,1,cross)

# createing track bars for rgb
cv2.createTrackbar("R","Color Picker by Aakash",0,255,cross)
cv2.createTrackbar("G","Color Picker by Aakash",0,255,cross)
cv2.createTrackbar("B","Color Picker by Aakash",0,255,cross)

while True:
    
    cv2.imshow("Color Picker by Aakash",img)
    k= cv2.waitKey(1) &0xFF
    if k == 27:
        break

    # now get trackbars pos
    s = cv2.getTrackbarPos(swith,"Color Picker by Aakash")
    r = cv2.getTrackbarPos("R","Color Picker by Aakash")
    g = cv2.getTrackbarPos("G","Color Picker by Aakash")
    b = cv2.getTrackbarPos("B","Color Picker by Aakash")

    if s == 0:
        img[:] = 0 
    else:
        img[:] = [b,g,r]
        
    
cv2.destroyAllWindows()


 