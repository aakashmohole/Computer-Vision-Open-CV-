import cv2

cap = cv2.VideoCapture(0)
print(cap)

# fps = cap.get(cv2.CAP_PROP_FPS)
# hight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

# DIVX XVID MJPG X264 WMV1 WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")

out = cv2.VideoWriter("GrayVideo.mp4",fourcc,20.0,(640,480),0)

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame,(700,800))
        # flip the window
        frame = cv2.flip(frame,0)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',frame)
        cv2.imshow('gray',gray)
        
        # Writeing video here
        out.write(gray)
        
        if(cv2.waitKey(2)==27):
            break
cap.release()
out.release()
cv2.destroyAllWindows()