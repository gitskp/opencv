# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 16:17:10 2018

@author: Shrikant
"""
import cv2

imgpath = "C:\\Users\\Shrikant\\Desktop\\standard_test_images\\lena_color_256.tif"
img = cv2.imread(imgpath,1)
cv2.imshow('lena',img)
cv2.waitKey(0)
cv2.destroyAllWindows()