# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 20:09:41 2018

@author: Shrikant
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0) # capture the video, a live video will open

color = (0,255,0) # color is green 
line_width=4  # width of line
radius=50 # raidus of circle
point=(100,150) # point of circle


# A click function for mouse left button activity
def click(event,x,y,flags,param):
    global point,pressed
    if event == cv2.EVENT_LBUTTONDOWN: #left button down
        print("Pressed",x,y)
        point=(x,y)
        
cv2.namedWindow("Frame") # name of window
cv2.setMouseCallback("Frame",click) # call the click function 


while True:
    ret,frame = cap.read()
    frame= cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    cv2.circle(frame,point,radius,color,line_width) # it will create a green circle when a live video will generate
    cv2.imshow("Frame",frame)
    
    
    ch = cv2.waitKey(1) # wait for 1 milli second
    if ch & 0xFF == ord('q'): # if opearting sysstem is 64 bit then use 0xFF. Video will be play until we do not press character q
        break
    

cap.release()
cv2.destroyAllWindows()
