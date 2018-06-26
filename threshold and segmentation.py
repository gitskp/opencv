# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 22:45:59 2018

@author: Shrikant
"""

import numpy as np
import cv2

img = cv2.imread('img.jpg',0) # convert black and white
height,width=img.shape[0:2]
cv2.imshow("image",img)

binary = np.zeros([height,width,1],'uint8')
thresh=85

# Metho 1 : for segmenation .it is slow for segmenation
for row in range(0,height):
    for col in range(0,width):
        if img[row][col]>thresh:
            binary[row][col]=255

cv2.imshow("slow bbianry",binary)


# method 2: using threshhold
ret,thresh = cv2.threshold(img,thresh,255,cv2.THRESH_BINARY)
cv2.imshow("Threshold",thresh)



cv2.waitKey(0)
cv2.destroyAllWindows()
