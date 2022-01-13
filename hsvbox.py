#! /usr/bin/env python3
# https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html
# https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    r = 10
    lower_yellow = np.array([30-r, 100, 80])
    upper_yellow = np.array([30+r, 255, 255])
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    numYellow = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    for area in numYellow:
        (x,y,w,h) = cv2.boundingRect(area)
        cv2.rectangle(frame,(x,y),(x+w, y+h),(0,0,255),2)
    res = cv2.bitwise_and(frame,frame, mask=mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
