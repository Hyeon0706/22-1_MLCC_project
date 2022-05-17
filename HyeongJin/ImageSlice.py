from array import array
from tkinter import N
import cv2
import matplotlib.pyplot as plt
import sys  
import numpy as np
import PIL


#이미지 읽어오기
img = cv2.imread("C:\PythonImage\sample.tif")
img2 = cv2.imread("C:\PythonImage\sample3.tif")  
if img is None:
    sys.exit("Could not read the image.")
#불량품 이미지
slice1 = img[88:171, 236:257]
slice2 = img[78:170, 404:427]
#정상품 이미지
slice3 = img2[88:171, 236:257]
slice4 = img2[78:170, 404:427]



#사이즈 조정
slice1 = cv2.resize(slice1, dsize=(200, 488), interpolation=cv2.INTER_AREA)
slice2 = cv2.resize(slice2, dsize=(200, 488), interpolation=cv2.INTER_AREA)
slice3 = cv2.resize(slice3, dsize=(200, 488), interpolation=cv2.INTER_AREA)
slice4 = cv2.resize(slice4, dsize=(200, 488), interpolation=cv2.INTER_AREA)
#이미지모양값 구하기
height, width, colorsss = slice1.shape


#컬러영상의 히스토그램으로 표시
colors = ['b', 'g', 'r']
bgr_planes = cv2.split(slice1)

for (p, c) in zip(bgr_planes, colors):
    hist = cv2.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(hist, color=c)

'''    
#카운트 인트형
count = 0;
#영상의 픽셀 값 구하기?씌발제발되라
 
#phjblue = slice1[:, :, 0]
phjblue = slice1[:, :, 2]
phjgreen = slice1[:, :, 1]
phjred = slice1[:, :, 2]

print("count값은 : ")
print(count)

for iii in range(len(phjblue)):
    for jjj in range(len(phjblue[iii])):
        if phjblue[iii][jjj] != 0:
            count += 1
            

print("변경된 count값은 : ")
print(count)            
'''


    


#영상의 픽셀 값 구하기?씌발제발되라
 
'''
phjblue = slice1[:, :, 0] 
phjgreen = slice1[:, :, 1] 
phjred = slice1[:, :, 2] 
'''
#카운트 인트형
bluecount = 0;
greencount = 0;
redcount = 0;
for iii in range(len(slice1)):
    for jjj in range(len(slice1[iii])):
        if slice1[iii][jjj][0] > 254:
            bluecount += 1
        if slice1[iii][jjj][1] > 254:
            greencount += 1
        if slice1[iii][jjj][2] > 254:
            redcount += 1
            
print("총픽셀 수는 : ")
print(slice1.size/3)            
print("bluecount값은 : ")
print(bluecount)            
print("greencount값은 : ")
print(greencount)            
print("redcount값은 : ")
print(redcount)            


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
    

#화면에 출력
cv2.imshow("img", img)
cv2.imshow("slice1", slice1)
cv2.imshow("slice2", slice2)
cv2.imshow("img2", img2)
cv2.imshow("slice3", slice3)
cv2.imshow("slice4", slice4)

plt.show()


cv2.waitKey()
cv2.destroyAllWindows()




