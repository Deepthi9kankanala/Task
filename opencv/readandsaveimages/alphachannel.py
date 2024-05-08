import cv2 
img1=cv2.imread('C:/Users/dell/Desktop/opencv/smile.jpg',-1) #oalpha scale 
img1=cv2.resize(img1,(1280,700))#width,height
cv2.imshow("alpha  img",img1)
print("Image in original value==\n",img1)
