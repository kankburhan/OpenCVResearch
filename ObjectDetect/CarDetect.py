import cv2
import numpy as np

carxml = cv2.CascadeClassifier('car3.xml')
img = cv2.imread('cars.jpg')

cars = carxml.detectMultiScale(img, 1.3, 5)
for(x, y, w, h) in cars:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()