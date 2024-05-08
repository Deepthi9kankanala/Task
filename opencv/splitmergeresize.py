import cv2
import numpy as np


img=cv2.imread("C:/Users/dell/Desktop/opencv/smile.jpg",1)

img=cv2.resize(img,(600,400))

cv2.imshow("result",img)

print("shape==",img.shape) #returns a tuple of number of rows , clms and channels

print("no of pixels==",img.size) # returns total num of pixels

print("datatype",img.dtype) #datatype isobtaines

print("img type",type(img))



#split -return 3 channel of img like bgr
b,g,r=cv2.split(img)
cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)


#merge-mix channels

mr1=cv2.merge((r,g,b))
cv2.imshow('rgb',mr1)
mr2=cv2.merge((g,b,r))
cv2.imshow('gbr',mr2)

