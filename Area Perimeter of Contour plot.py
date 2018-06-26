# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 18:50:45 2018

@author: Shrikant
"""

import numpy as np
import cv2

img = cv2.imread("contour.png",1)
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY) # convert original image to gray image
thresh =  cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1) # convert ggray image to binary image
cv2.imshow("Binary",thresh)


_, contours,hierarchy =  cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img2 = img.copy() # copy of img

index=-1
thickness =4
color=(255,0,255)

objects = np.zeros([img.shape[0],img.shape[1],3],'uint8')
for c in contours:
    cv2.drawContours(objects,[c],-1,color,-1)
    area = cv2.contourArea(c) # area of each contour plot
    perimeter = cv2.arcLength(c,True) # perimeter each contour plot
    
    M= cv2.moments(c) # moments of c objects
    cx = int(M['m10']/M['m00']) # middle points of objects
    cy= int(M['m01']/M['m00']) # middle points of objects
    cv2.circle(objects,(cx,cy),4,(0,0,255),-1) # drae the circle and fill dircle
    print("Area:{},Perimeter:{}".format(area,perimeter)) # Area and Perimeetr of each plot in contours object
cv2.imshow("Contours",objects)  # show the contours image

cv2.waitKey(0)
cv2.destroyAllWindows()
