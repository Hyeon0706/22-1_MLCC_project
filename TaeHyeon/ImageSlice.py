from array import array
from tkinter import N
import cv2
import matplotlib.pyplot as plt
import sys  
import numpy as np
import PIL

#밝기검출 함수
def check_color(side_perfection, middle_perfection, left_side, right_side, middle_side):
    result = True
    left_redcount = 0
    right_redcount = 0
    middle_redcount = 0
    side_perfection = (100 - side_perfection)
    middle_perfection = (100 - middle_perfection)
    for iii in range(len(left_side)):
        for jjj in range(len(left_side[iii])):
            if left_side[iii][jjj][2] > 254:
                left_redcount += 1
        
    for iii in range(len(right_side)):
        for jjj in range(len(right_side[iii])):
            if right_side[iii][jjj][2] > 254:
                right_redcount += 1
    
    for iii in range(len(middle_side)):
        for jjj in range(len(middle_side[iii])):
            if middle_side[iii][jjj][2] > 254:
                middle_redcount += 1        
                                    
    if (((left_side.size /3) / left_redcount) / 100 >= side_perfection) or (((right_side.size /3) / right_redcount) / 100 >= side_perfection):
        result = False
    
    if (((middle_side.size /3) / middle_redcount) / 100 >= middle_perfection):
        result = False
       
    return result
 
    
# or (((middle_side.size /3) / middle_redcount) / 100 >= perfection)

'''
p = img[80, 80, 2]
    

#실패작 시발
for j in range(height):

    for i in range(width):
       pointPixel = slice1.item(i, j, 0)
       print(pointPixel)
       print()
       if slice1.item(i, j, 0) != 0 :
           phjblue += 1
           print(phjblue)
       

'''

    
    
'''
각영상의 히스토그램 예제
bgr_planes = cv2.split(slice1)

for (p, c) in zip(bgr_planes, colors):
    hist = cv2.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(hist, color=c)
    
bgr_planes = cv2.split(slice2)

for (p, c) in zip(bgr_planes, colors):
    hist = cv2.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(hist, color=c)
    
bgr_planes = cv2.split(slice3)

for (p, c) in zip(bgr_planes, colors):
    hist = cv2.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(hist, color=c)

bgr_planes = cv2.split(slice4)

for (p, c) in zip(bgr_planes, colors):
    hist = cv2.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(hist, color=c)        

'''





