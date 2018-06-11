import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8) # create image using numpy means value pixel
#cv2.imshow("Black Image",img)
cv2.line(img,(0,100),(100,0),(255,0,0),2)
cv2.rectangle(img,(100,80),(200,190),(0,255,0),2)
cv2.circle(img,(80,80),50,(0,0,255),-1)
cv2.ellipse(img,(160,280),(50,70),0,0,360,(127,127,127),-1)
text1 = "Hello opencv"
cv2.putText(img,text1,(100,100),cv2.FONT_HERSHEY_SIMPLEX,5,(255,255,0))

cv2.imshow('lena',img)


cv2.waitKey(0)
cv2.destroyWindow('lena')

