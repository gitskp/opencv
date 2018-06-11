# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 16:54:44 2018

@author: Shrikant
"""

import cv2

imgpath = "C:\\Users\\Shrikant\\Desktop\\standard_test_images\\lena_color_256.tif"
img = cv2.imread(imgpath,0) # convert original image to gray image
output_path = "C:\\Users\\Shrikant\\Desktop\\output\\lena_color_256.jpg"
cv2.imshow('Lena',img)
cv2.imwrite(output_path,img)
cv2.waitKey()
cv2.destroyWindow('Lena')


