import cv2 
img1=cv2.imread('C:/Users/dell/Desktop/opencv/smile.jpg',1) #original img 
img1=cv2.resize(img1,(1280,700))#width,height
cv2.imshow("original img",img1)
cv2.imwrite("keepsmiling.jpg",img1)
