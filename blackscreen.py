import cv2
import numpy as np


video = cv2.VideoCapture(0)
image = cv2.imread("backgroundimg1.jpeg")


while(video.isOpened()):
   
    ret, frame = video.read()

    image = cv2.resize(image, (640, 480))
    frame = cv2.resize(frame, (640,480))
   
    upper_black = np.array([104,153,70])
    lower_black = np.array([30,30,0])

 
    mask = cv2.inRange(frame, lower_black, upper_black)
    forg = cv2.bitwise_and(frame, frame, mask= mask)
   
    part = frame - forg 
    part = np.where(part == 0, image, part)

    output = cv2.addWeighted(part, 1, image, 0, 0)

    cv2.imshow("background", output)
    key = cv2.waitKey(1)

video.release()
cv2.destroyAllWindows()