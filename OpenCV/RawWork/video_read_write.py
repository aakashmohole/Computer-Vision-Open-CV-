import cv2

# instance video capturing and 0 for default web camp
cap = cv2.VideoCapture(0)

# check camera is opened or not
opened = cap.isOpened()

#fourcc - four character code for determining the codec of the video file
fourcc = cv2.VideoWriter_fourcc(*'MJPG')

# get hight width and fps
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
fps = cap.get(cv2.CAP_PROP_FPS)

# write video
out = cv2.VideoWriter('myVideo.avi', fourcc,fps ,(int(width), int(height)))

print("hight are: {}".format(height))
print("width are: {}".format(width))
print("Frames are: {}".format(fps))

#Showing and storing the live camera feed
#Check if camera is opened
if(opened):
	#Run until it remains open
	while(cap.isOpened()):
		#Get the frame from Video capture Instance
		ret, frame = cap.read()
		#
		#return ret Variable tells if the frame is returned successfully
		if(ret==True):
			cv2.imshow('myVideoCaptureWindow', frame)
			#Writing the frame to video output
			out.write(frame)
			#Wait for 2 milliseconds for each frame 
			#If user press 'esc' key then exit loop
			if(cv2.waitKey(2)==27):
				break
out.release()
cap.release()
cv2.destroyAllWindows()