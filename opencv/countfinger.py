import cv2
import time
import os
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

folderpath = 'fingerimages'
mylist = os.listdir(folderpath)
print(mylist)
overlaylist = []

for impath in mylist:
    image = cv2.imread(f'{folderpath}/{impath}')
    overlaylist.append(image)
print(len(overlaylist))

ptime = 0

detector = htm.handDetector(detectionCon=0.75)

tipids = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    if not success:
        break

    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)

    if len(lmlist) != 0:
        fingers = []

        # Thumb
        if lmlist[tipids[0]][1] < lmlist[tipids[0] - 1][1]:  # Thumb tip is to the left of the previous joint
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 fingers
        for id in range(1, 5):
            if lmlist[tipids[id]][2] < lmlist[tipids[id] - 2][2]:  # Up
                fingers.append(1)
            else:
                fingers.append(0)

        totalfingers = fingers.count(1)
        print(totalfingers)

      
        if 0 < totalfingers <= len(overlaylist):
            h, w, c = overlaylist[totalfingers - 1].shape
            img[0:h, 0:w] = overlaylist[totalfingers - 1]

        cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(totalfingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
