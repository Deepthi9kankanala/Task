import cv2 
img1=cv2.imread('C:/Users/dell/Desktop/opencv/smile.jpg',0) #grayscale
img1=cv2.resize(img1,(1280,700))#width,height
cv2.imshow("grayscaleimg",img1)
