import cv2
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)# 0 is path of any video from webcam
print("check===",cap.isOpened())
#it is 4 byte code which in use to specify the video code
# various codec-- DIVX,XVID,MJPG,X264,WMV1,WMV2
fourcc=cv2.VideoWriter_fourcc(*"XVID")
# it contain 4 param ,anme , codec,fps,resolution
output=cv2.VideoWriter("videowebcam.mp4",fourcc,20.0,(640,480),0)
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frame=cv2.flip(frame,1) #0,-1,1
        output.write(gray)
        cv2.imshow("Gray Frame:",gray)
        cv2.imshow("Color Frame",frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
cap.release()
output.release()
cv2.destroyAllWindows()
    
"""


2. `print("check===", cap.isOpened())`: This line checks if the capture object (`cap`) was successfully initialized by verifying if it's opened.

3. `fourcc=cv2.VideoWriter_fourcc(*"XVID")`: This line defines the codec to be used for writing the video. Here, it's set to XVID, which is a widely used codec for video compression.

4. `output=cv2.VideoWriter("videowebcam.mp4", fourcc, 20.0, (640,480), 0)`: This initializes a VideoWriter object to write the video to a file named "videowebcam.mp4". The parameters are:
   - Filename: Name of the output file.
   - FourCC: Codec to be used for compression.
   - FPS: Frames per second.
   - Resolution: Width and height of the video frame.
   - isColor: Flag indicating whether the output is a color video (0 for grayscale).

5. `while(cap.isOpened()):`: This starts a loop to continuously capture frames from the webcam until the capture object is open.

6. `ret, frame = cap.read()`: This line reads a frame from the webcam. `ret` is a boolean indicating if the frame was successfully read, and `frame` contains the captured frame.

7. `if ret==True:`: Checks if a frame was successfully read.

8. `gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)`: Converts the color frame (`frame`) to grayscale (`gray`) using the `cvtColor` function.

9. `frame = cv2.flip(frame, 1)`: Flips the color frame horizontally (around the y-axis) using the `flip` function. This creates a mirror effect.

10. `output.write(gray)`: Writes the grayscale frame (`gray`) to the output video file.

11. `cv2.imshow("Gray Frame:", gray)`: Displays the grayscale frame in a window titled "Gray Frame".

12. `cv2.imshow("Color Frame", frame)`: Displays the color frame in a window titled "Color Frame".

13. `if cv2.waitKey(1) & 0xFF == ord('q'): break`: Checks if the 'q' key is pressed. If so, it breaks out of the loop and ends the program.

14. `cap.release()`: Releases the capture object, releasing the webcam.

15. `output.release()`: Releases the VideoWriter object, closing the output video file.

16. `cv2.destroyAllWindows()`: Closes all OpenCV windows."""
