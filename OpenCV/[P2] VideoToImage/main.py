import cv2

vidcap = cv2.VideoCapture("D:\\OpenCV\\VideoToImageP3\\sample.mp4")

ret, image = vidcap.read()

count = 0

while True:
    if ret == True:
        cv2.imwrite("D:\\OpenCV\\VideoToImageP3\\images\\img%d.png"%count,image)
        time_in_milliseconds = 1000 * count 
        vidcap.set(cv2.CAP_PROP_POS_MSEC, time_in_milliseconds)
        ret,image = vidcap.read()
        
        count += 1
        
        print(count)
        if cv2.waitKey(2) == 27:
            break
            cv2.destroyAllWindows()
            
vidcap.release()
cv2.destroyAllWindows()