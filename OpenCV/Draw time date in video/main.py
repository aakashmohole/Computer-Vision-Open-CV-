import cv2
import datetime
vid = cv2.VideoCapture("D:\\OpenCV\\ReadWrite\\Draw time date in video\\sample.mp4")

# print("width = ",vid.get(cv2.CAP_PROP_FRAME_WIDTH))
# print("hight = ",vid.get(cv2.CAP_PROP_FRAME_HEIGHT))

# here 3 for width and 4 for hight
print("width = "+str(vid.get(3)))
print("hight = "+str(vid.get(4)))

# get higt and widt in var 
font = "width: " + str(vid.get(3)) + " hight : "+str(vid.get(4)) 
date_time = "Date: " + str(datetime.datetime.now())

while vid.isOpened():
    ret ,frame = vid.read()
    if ret == True:
        
        frame = cv2.resize(frame,(900,500))

        # here we put hight width in video
        frame = cv2.putText(frame,font,(50,450),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),1,cv2.LINE_AA)
        #here we sett current date time
        frame = cv2.putText(frame,date_time,(20,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),1,cv2.LINE_AA)
                
        cv2.imshow('windname',frame)
        if cv2.waitKey(25) ==27:
            break
    else:
        break
vid.release()
cv2.destroyAllWindows()




