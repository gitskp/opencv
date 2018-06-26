# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 17:48:23 2018

@author: Shrikant
"""

import numpy as np
import cv2
color = cv2.imread("img.jpg")


gray = cv2.cvtColor(color,cv2.COLOR_RGB2GRAY) # convert original image to gray image
cv2.imwrite("gray.jpg",gray)
b = color[:,:,0] # channel 1
g = color[:,:,1] # channel 2
r = color[:,:,2] # channel 3

rgba = cv2.merge((b,g,r,g))
cv2.imwrite("rbga.png",rgba)




