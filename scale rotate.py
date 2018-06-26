# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:22:54 2018

@author: Shrikant
"""

import numpy as np
import cv2

# read the image
img = cv2.imread("img2.jpg",1)

# scale the image
img_half = cv2.resize(img,(0,0),fx=0.5,fy=0.5) # half of the image
img_strech = cv2.resize(img,(600,600))  # streching of the image
img_strech_near = cv2.resize(img,(600,600),interpolation=cv2.INTER_NEAREST) # nearest streach of image

cv2.imshow("Half Image",img_half)
cv2.imshow("Streach of image",img_strech)
cv2.imshow("Streach image near",img_strech_near)


# Rotation
m= cv2.getRotationMatrix2D((0,0),-30,1)
rotated = cv2.warpAffine(img,m,(img.shape[1],img.shape[0]))
cv2.imshow("Roated",rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()

