import cv2
import numpy as np

# take black background
# img =  np.zeros([512,512,3],np.uint8)*255

# take white background
img =np.ones([512,512,3],np.uint8)*255

# take image as background
# img = cv2.imread("D:\\OpenCV\\ReadWrite\\BasicShapes\\img.jpg")

# here line take 5 parameters (img,x y starting point,x y  ending point, colour in BGR, thiskness)
img = cv2.line(img,(0,0),(200,200),(200,20,255),5)

# here rectangle take 5 parameters (img,x y starting point,x y  ending point, colour in BGR, thiskness)
img = cv2.rectangle(img,(180,100),(310,285),(230,0,0),5)

# here arrowed line take 5 parameters (img,x y starting point,x y  ending point, colour in BGR, thiskness)
img =  cv2.arrowedLine(img,(10,10),(150,200),(0,0,255),10)

# here circle take 5 parameters (img,x y center point,radius, colour in BGR, thiskness)
img = cv2.circle(img,(247,225), 150,(0,255,0),8)

# here text take 8 parameters (img,text,start cor, font,font size, colour in BGR, thiskness, line tyepe)
img = cv2.putText(img,"Aakash",(100,310),cv2.FONT_ITALIC,2,(0,125,255),5,cv2.LINE_AA)

# here ellips take 5 parameters (img,text,start cor, (length,hight), colour in BGR, thiskness, line tyepe)
img = cv2.ellipse(img,(200,400),(100,50),0,0,270,200,2)

cv2.imshow("new",img)
cv2.waitKey(5000)
cv2.destroyAllWindows()