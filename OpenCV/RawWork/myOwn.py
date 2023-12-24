import cv2
cap = cv2.VideoCapture(0)

fps = cap.get(cv2.CAP_PROP_FPS)
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

fourcc = cv2.VideoWriter_fourcc(*'MJPG')

out = cv2.VideoWriter('newvideo.avi',fourcc,fps,(int(w),int(h)))

while cap.isOpened():
    ret ,frames = cap.read()
    if ret == True:
        cv2.imshow('live_window',frames)
        out.write(frames)
        
        if(cv2.waitKey(2)) ==27:
            break 
cap.release()
out.release()
cv2.destroyAllWindows()   