import cv2
import numpy as np

img = np.zeros((400,400,3),dtype=np.uint8)

lines = np.array([[200, 200,
                   200 + (200 * np.cos(np.pi / 4)),200 + (200 * np.sin(np.pi / 4))],
                   [200, 200,
                   200 + (200 * np.cos(np.pi)), 200 + (200 * np.sin(np.pi))],
                  [200, 200,
                   200 + (200 * np.cos(np.pi * 7 / 4)), 200 + (200 * np.sin(np.pi * 7 / 4))],
                  [200, 200,
                   200 + (200 * np.cos(np.pi * 8 / 4)), 200 + (200 * np.sin(np.pi * 8 / 4))]],dtype=np.int32)
slope_degree = (np.arctan2(lines[:,1]-lines[:,3],lines[:,0]-lines[:,2])*180)/np.pi

print(slope_degree)

for line in lines:
    cv2.line(img,(line[0],line[1]),(line[2],line[3]),[255,0,0],2)

cv2.imshow('img',img)
cv2.waitKey(0)