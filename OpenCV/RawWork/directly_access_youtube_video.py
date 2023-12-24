import cv2
import pafy

url = "https://youtu.be/CgM_2ERkZiQ?si=1m4-nU21sXIxfGwo"

# store data include in rul in data var
data = pafy.new(url)
data = data.getbest(preftype="mp4") #prefered type mp4

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.open(data.url)

print("Check = ",cap.isOpened())

while(cap.isOpened()):
    rat,frame = cap.read()
    if rat == True:
        frame = cv2.resize(frame,(600,600))
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2LAB)
        
        cv2.imshow('myWindow',frame)
        cv2.imshow('myGray',gray)
        
        if cv2.waitKey(2) == 27:
            break
        
cap.release()
cv2.destroyAllWindows()


# ERROR IN YOUTUBNE_DL 