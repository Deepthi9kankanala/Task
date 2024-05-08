#draw shapes

import cv2
img=cv2.imread('C:/Users/dell/Desktop/opencv/smile.jpg',1)
img=cv2.resize(img,(700,800))
            #img,strat   ,end,           color, thickness
img=cv2.line(img,(0,0),(400,400),(154,92,300),8)
img1=cv2.arrowedLine(img,(0,0),(40,40),(54,92,30),2)
rec=cv2.rectangle(img,(100,10),(510,510),(128,0,255),8)
#img,start,radius,color,thick
cir=cv2.circle(img,(447,125),63,(215,255,0),-5)
#img,texr.start,font,size,color,thickness,linetype
text=cv2.putText(img,'Hey Smilyyy',(20,500),cv2.FONT_ITALIC,4,(0,125,255),10,cv2.LINE_AA)
#img.start,(len,height),color,thickness
ellipse=cv2.ellipse(img,(400,600),(100,50),0,0,180,155,5)
cv2.imshow("Itslined", img)
cv2.imshow("Itsarrowedlined", img1)
cv2.imshow("rect",rec)
cv2.imshow("cir",cir)
cv2.imshow('text',text)
cv2.imshow('ellipse',ellipse)



