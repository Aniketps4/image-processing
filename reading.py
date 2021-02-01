# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 12:07:25 2021

@author: anike
"""

import numpy as np
import cv2
img = cv2.imread('cat.jpg',1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)