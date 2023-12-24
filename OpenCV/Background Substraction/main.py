import cv2
import numpy as np
#Background Subtraction is a way to access the foreground objects.
#Technically, you need to extract the moving 
#foreground from static background.
#There are multiple approach for backgroud subtract

cap = cv2.VideoCapture("D:\\OpenCV\\RawWork\\Background Substraction\\test2.mp4")

algo1 = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
algo2 = cv2.createBackgroundSubtractorKNN(detectShadows=True)


while True:
    if cap.isOpened():
        ret, frames = cap.read()
        frames = cv2.resize(frames,(600,600))
        
        res1 = algo1.apply(frames) 
        res2 = algo2.apply(frames)
        
        cv2.imshow('orig',frames)
        cv2.imshow('res1',res1)
        cv2.imshow('res2',res2)
        
        k = cv2.waitKey(25)
        if k == 27:
            break

cv2.destroyAllWindows()
