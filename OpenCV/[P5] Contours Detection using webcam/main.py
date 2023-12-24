import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def nothing():
    pass

cv2.namedWindow('flag')
cv2.resizeWindow('flag',(300,300))
cv2.createTrackbar('threshold','flag',0,255,nothing)

# color detection trackbars
cv2.createTrackbar('Upper_h','flag',255,255,nothing)
cv2.createTrackbar('Upper_s','flag',255,255,nothing)
cv2.createTrackbar('Upper_v','flag',255,255,nothing)

cv2.createTrackbar('Lower_h','flag',0,255,nothing)
cv2.createTrackbar('Lower_s','flag',0,255,nothing)
cv2.createTrackbar('Lower_v','flag',0,255,nothing)

while True:
    if cap.isOpened():
        ret, frame = cap.read()
        frame = cv2.resize(frame,(400,400))
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        upper_h = cv2.getTrackbarPos('Upper_h','flag')
        upper_s = cv2.getTrackbarPos('Upper_s','flag')
        upper_v = cv2.getTrackbarPos('Upper_v','flag')
        
        lower_h = cv2.getTrackbarPos('Lower_h','flag')
        lower_s = cv2.getTrackbarPos('Lower_s','flag')
        lower_v = cv2.getTrackbarPos('Lower_v','flag')
         
         
        lower_bound = np.array([lower_h,lower_s,lower_v])
        upper_bound = np.array([upper_h,upper_s,upper_v])

        # create mask
        mask = cv2.inRange(hsv,lower_bound,upper_bound)
        # create filter
        filtr = cv2.bitwise_and(frame, frame, mask=mask)

        mask1  = cv2.bitwise_not(mask)
        m_g = cv2.getTrackbarPos("threshold", "flag") #getting track bar value
        ret,thresh = cv2.threshold(mask1,m_g,255,cv2.THRESH_BINARY)
        dilata = cv2.dilate(thresh,(1,1),iterations = 6)
        
        #findcontour(img,contour_retrival_mode,method)
        cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #Here cnts is a list of contours. ANd each contour is an array with x, y cordinate   
        #hier variable called hierarchy and it contain image information.
        #print("Number of contour==",cnts,"\ntotal contour==",len(cnts))
        #print("Hierarchy==\n",hier)
        
        #Draw the contours
        #frame= cv2.drawContours(frame,cnts,-1,(176,10,15),4)
        
        # loop over the contours
        
        for c in cnts:
            epsilon = 0.0001*cv2.arcLength(c,True)
            data= cv2.approxPolyDP(c,epsilon,True)
        
            hull = cv2.convexHull(data)
            cv2.drawContours(frame, [c], -1, (50, 50, 150), 2)
            cv2.drawContours(frame, [hull], -1, (0, 255, 0), 2)
            """
            hull = cv2.convexHull(data,returnPoints = False)
            defect = cv2.convexityDefects(data[0],hull)
            print("defect==",defect)
            """
        cv2.imshow("Thresh", thresh)
        cv2.imshow("mask==",mask)
        cv2.imshow("filter==",filtr)
        cv2.imshow("Result", frame)

        key = cv2.waitKey(25) &0xFF
        if key == 27:
            break
cap.release()
cv2.destroyAllWindows()
    
        