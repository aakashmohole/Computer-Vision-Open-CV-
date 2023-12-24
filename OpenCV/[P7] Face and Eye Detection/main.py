import cv2 as cv
import numpy as np

# face detection using haarcascade
face = cv.CascadeClassifier('D:\\OpenCV\\[P9] Face and Eye Detection\\haarcascade_frontalface_default.xml')
eye = cv.CascadeClassifier('D:\\OpenCV\\[P9] Face and Eye Detection\\haarcascade_eye.xml') #for detecting eyes

print(face)
image=cv.imread("D:\\OpenCV\\[P9] Face and Eye Detection\\img3.jpg")
gray= cv.cvtColor(image,cv.COLOR_BGR2GRAY) #convert into gray 

faces = face.detectMultiScale(gray, scaleFactor=2, minNeighbors=3)


for (x,y,w,h) in faces:
    image = cv.rectangle(image,(x,y),(x+w,y+h),(0,0,255),3)

     #Now detect eyes
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    eyes = eye.detectMultiScale(roi_gray,1.2,3)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


image = cv.resize(image,(400,500))
# cv.imshow("Face",res)
cv.imshow("Face Detected",image)
cv.waitKey(0)
cv.destroyAllWindows()    



