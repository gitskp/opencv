# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:45:13 2018

@author: Shrikant
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0) # capture the video, a live video will open

while True:
    ret,frame = cap.read()
    frame= cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    cv2.imshow("Frame",frame)
    
    
    ch = cv2.waitKey(1) # wait for 1 milli second
    if ch & 0xFF == ord('q'): # if opearting sysstem is 64 bit then use 0xFF. Video will be play until we do not press character q
        break
    

cap.release()
cv2.destroyAllWindows()

    