import numpy as np
import cv2

#capture vide0
cap = cv2.VideoCapture(0)

while(True):
    #Capture frame by frame
    ret, frame = cap.read()

    #Change capture to gray color
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Display the resulting frame
    #cv2.imshow('frame', gray)

    #normal Color
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#when everything done, release capture
cap.release()
cv2.destroyAllWindows()    
