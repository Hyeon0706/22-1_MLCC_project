import cv2
import load

img = cv2.imread('001-1.tif')

cv2.imshow('right', load.sliceEle1(img))
cv2.imshow('left', load.sliceEle2(img))
cv2.waitKey(0)
cv2.destroyAllWindows()