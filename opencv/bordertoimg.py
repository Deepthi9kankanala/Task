# Border for an image using opencv


# with help of cv2.copyMakeBorder() fn
#parameters (img,border_width*4,bordertype,val_border)

#border_width=top,bottom,right,left

import cv2
import numpy as np

im=cv2.imread("C:/Users/dell/Desktop/opencv/smile.jpg",1)
im=cv2.resize(im,(1000,600))

brdr=cv2.copyMakeBorder(im,10,10,5,5,cv2.BORDER_CONSTANT,value=[255,0,125])

cv2.imshow("borderimg",brdr)
cv2.waitKey(0)
cv2.destroyAllWindows()
