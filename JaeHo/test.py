import cv2
import load

img = cv2.imread('001-1.tif')

cv2.imshow('right', load.loadRightEle(img))
cv2.imshow('left', load.loadLeftEle(img))
cv2.waitKey(0)
cv2.destroyAllWindows()