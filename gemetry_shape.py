# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 17:50:08 2018

@author: Shrikant
"""

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8) # create image using numpy means value pixel
cv2.imshow("Black Image",img)

cv2.waitKey(0)
cv2.destroyWindow
