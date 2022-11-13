# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 09:05:19 2022

@author: user
"""
#greyscale image
import cv2 
import matplotlib.pyplot as plt


img = cv2.imread(cv2.samples.findFile("C:/Users/user/new/New folder/crab.jpeg"))
img = cv2.resize(img, (128, 64))
g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
image = g

fig, ax = plt.subplots()
plt.imshow(g, cmap="gray")

