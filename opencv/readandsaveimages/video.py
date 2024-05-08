import cv2
cap=cv2.VideoCapture("C:/Users/dell/Desktop/opencv/video.mp4")
while True:
    ret,frame=cap.read()#read frame
    frame=cv2.resize(frame,(500,500))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Colorframe',frame)
    cv2.imshow('Gray frame',gray)
    if cv2.waitKey(25) & 0xff==ord('q') :#pres exit
        #waits for a key event for 25 milliseconds. If a key is        ressed within this time, it returns the ASCII value of the key.
         #& 0xff: This is a bitwise AND operation with 0xff, which is 11111111 in binary. This operation helps to extract the last 8 bits (or the least significant byte) of the return value, which is usually the ASCII code of the key pressed.
          #== ord('q'): This part checks if the key pressed is 'q'. ord('q') returns the ASCII value of the character 'q'. If the pressed key matches 'q', the condition evaluates to True.
        break
#release everything if job finished
cap.release()
cv2.destroyAllWindows() 
