#!/usr/bin/env python3
# https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
# https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html
# https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # template = cv.imread('carmex.png',0)
    # template = cv.imread('charge.png',0)
    template = cv.imread('ball.png',0)
    w,h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.6
    loc = np.where( res >= threshold )
    for pt in zip(*loc[::-1]):
        cv.rectangle(frame, pt, (pt[0] + w, pt[1]+h), (0,0,255), 2)
    cv.imshow('frame',frame)

    # close window
    k = cv.waitKey(5) & 0xFF
    if k == ord('q'):
        break
cv.destroyAllWindows()
