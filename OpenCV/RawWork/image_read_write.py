import cv2

image = cv2.imread('ReadWrite\\img.jpg')

if image is not None:
    print("Image Loaded successfully")
    cv2.imshow('image read window',image)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
else:
    print("image not found")