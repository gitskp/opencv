# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 18:13:00 2018

@author: Shrikant
"""

import numpy as np
import cv2
image = cv2.imread("img.jpg")
cv2.imshow("Original images",image)

blur = cv2.GaussianBlur(image,(5,55),0) # convert origina image to blur image
cv2.imshow("blur image",blur) # show the blur image

kernal = np.ones((5,5),'uint8') # this is kernal size of 5*5

dilate = cv2.dilate(image,kernal,iterations=1) # dilate convert whatever background image pixel into white pixel

erode = cv2.erode(image,kernal,iterations=1) # erode function convert white pixel to black pixel

cv2.imshow("Dilate",dilate) # show Dilate the image 
cv2.imshow("Erode",erode) # show Erode the image 

cv2.waitKey(0)
cv2.destroyAllWindows()







