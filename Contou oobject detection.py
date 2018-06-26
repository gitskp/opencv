# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:57:58 2018

@author: Shrikant
"""

import numpy as np
import cv2

img = cv2.imread("contour.png",1)
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY) # convert original image to gray image
thresh =  cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1) # convert ggray image to binary image
#cv2.imshow("Binary image",thresh)

_, contours,hierarchy =  cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img2 = img.copy() # copy of img

index=-1
thickness =4
color=(255,0,255)

cv2.drawContours(img2,contours,index,color,thickness)
cv2.imshow("Contours",img2)


cv2.waitKey(0)
cv2.destroyAllWindows()
