# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 12:25:16 2021

@author: anike
"""

import numpy as np
import cv2
img1 = cv2.imread('cat.jpg')
h,w,bpp = np.shape(img1)
img_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img2=cv2.merge((img_gray,img_gray,img_gray))
th1, img3 = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)
img4 = cv2.resize(img1,None,fx=0.1, fy=0.1, interpolation = cv2.INTER_AREA)
img4 = cv2.resize(img4,None,fx=10, fy=10, interpolation = cv2.INTER_AREA)
img5 = cv2.GaussianBlur(img1,(9,9),10)
img6 = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
temp1 = np.concatenate((img1,img2,img3), axis=1)
temp2 = np.concatenate((img4,img5,img6), axis=1)
img_final = np.concatenate((temp1,temp2), axis=0)
cv2.imshow("result",img_final)
cv2.waitKey(0)
cv2.destroyAllWindows()