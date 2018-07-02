# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 12:29:59 2018

@author: Shrikant
"""

import cv2
import numpy as np
import random

img_ball = cv2.imread("football.jpg",0)
img_player = cv2.imread("player.jpg",0)
cv2.imshow("football",img_ball)
cv2.imshow("player",img_player)


result = cv2.matchTemplate(img_ball,img_player,cv2.TM_CCOEFF_NORMED)
min_val,max_val,min_loc,max_loc=cv2.minMax(result)
print(max_val.max_loc)
cv2.circle(result,max_loc,15,255,2)
cv2.imshow("Matching",result)

cv2.waitKey(0)
cv2.destroyAllWindows()
