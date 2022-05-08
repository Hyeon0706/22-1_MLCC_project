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
        if slice1[iii][jjj][0] > 250:
            bluecount += 1
        if slice1[iii][jjj][1] > 250:
            greencount += 1
        if slice1[iii][jjj][2] > 250:
            redcount += 1
            

print("변경된 bluecount값은 : ")
print(bluecount)            
print("변경된 greencount값은 : ")
print(greencount)            
print("변경된 redcount값은 : ")
print(redcount)            

#print(phjgreen)
#print(phjred)


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
    
'''
#화면에 출력
cv2.imshow("img", img)
cv2.imshow("slice1", slice1)
cv2.imshow("slice2", slice2)
cv2.imshow("img2", img2)
cv2.imshow("slice3", slice3)
cv2.imshow("slice4", slice4)
'''
plt.show()


cv2.waitKey()
cv2.destroyAllWindows()




