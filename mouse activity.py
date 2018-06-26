# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 20:40:52 2018

@author: Shrikant
"""

import numpy as np
import cv2

# Global variables
canvas = np.ones([500,500,3],'uint8')*255
radius =3
color=(0,255,0)
pressed = False


# A click function for mouse left button activity
def click(event,x,y,flags,param):
    global canvas,pressed
    if event == cv2.EVENT_LBUTTONDOWN: #left button down
        pressed = True
        cv2.circle(canvas,(x,y),radius,color,-1)
    elif event == cv2.EVENT_MOUSEMOVE and pressed==True:
        cv2.circle(canvas,(x,y),radius,color,-1)
        print("Mouse moove")
    elif event==cv2.EVENT_LBUTTONUP:
        pressed = False
        
        
        
cv2.namedWindow("canvas") # name of window
cv2.setMouseCallback("canvas",click) # call the click function 


while True:
    
    cv2.imshow("canvas",canvas)
    
    
    ch = cv2.waitKey(1) # key capture every 1 ms
    if ch & 0xFF == ord('q'): # if opearting sysstem is 64 bit then use 0xFF. Video will be play until we do not press character q
        break
    elif ch & 0xFF ==ord('r'):
        color=(0,0,255)
    elif ch & 0xFF ==ord('g'):
        color=(0,255,0)
    elif ch & 0xFF ==ord('b'):
        color=(255,0,0)
    


cv2.destroyAllWindows()
