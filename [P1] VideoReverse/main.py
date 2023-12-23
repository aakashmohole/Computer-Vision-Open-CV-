import cv2

cap = cv2.VideoCapture('D:\\OpenCV\\VideoReverseP2\\sampleVideo.mp4')

#get frame count
frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

#get fps 
fps = cap.get(cv2.CAP_PROP_FPS)

#get hight width
hight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

#create fourcc
fourcc = cv2.VideoWriter_fourcc(*'MJPG')

#creat output video writer
out = cv2.VideoWriter('reversed.avi',fourcc,fps,(int(width),int(hight)))

print("no of frames: {}".format(frames))
print("no of fps: {}".format(fps))

# get frame index to reveres the video
frame_ind = frames-1

# check video instance 
if(cap.isOpened()):
    while(frame_ind != 0):
        # here we set current fram posi to last frame
        # reading the frames till end of the video
        cap.set(cv2.CAP_PROP_POS_FRAMES,frame_ind)
        ret,frame = cap.read()
        
        # resize frame if needed not neccesarry
        frame = cv2.resize(frame,(int(width*0.5),int(hight*0.5)))
        
        #potional- to show the revers video
        # cv2.imshow('windname',frame)

        #write revers video in outpot instance
        out.write(frame)
        
        # decrement frame index by 1 at each step
        frame_ind = frame_ind-1
        
        # print progress
        if(frame_ind%100 == 0):
            print(frame_ind)
            
out.release()
cap.release()
cv2.destroyAllWindows()    
    
    




