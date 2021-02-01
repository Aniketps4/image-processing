# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 12:13:10 2021

@author: anike
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('cat.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis 
plt.show()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)