import numpy as np  #import numpy module
import cv2          #import opencv2 module

#load normal image 
#img = cv2.imread('raisha.jpg')  

#make image grey
imggrey = cv2.imread('raisha.jpg', 0)

#display image
#cv2.imshow('img', img)
cv2.imshow('img', imggrey)
k = cv2.waitKey(0)
if k == 27: #esc button will close this image
    cv2.destroyAllWindows()
elif k == ord('s'): #press s
    cv2.imwrite('raishacantik.png', imggrey) #save new file
    cv2.destroyAllWindows()
    