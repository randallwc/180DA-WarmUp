#!/usr/bin/env python3
# https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of yellow color in HSV
    r = 10
    lower_yellow = np.array([30-r, 100, 80])
    upper_yellow = np.array([30+r, 255, 255])
    # Threshold the HSV image to get only yellow colors
    mask = cv.inRange(hsv, lower_yellow, upper_yellow)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
