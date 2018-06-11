# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 17:38:14 2018

@author: Shrikant
"""

import cv2

imgpath = "C:\\Users\\Shrikant\\Desktop\\standard_test_images\\lena_color_256.tif"
img = cv2.imread(imgpath,0) # convert original image to gray image
print(img)
print(type(img))
print(img.dtype)
cv2.imshow('Lena',img)
cv2.waitKey(0)
cv2.destroyWindow('Lena')