import cv2
import sys


img = cv2.imread('001-1.tif')
                                
blur = cv2.GaussianBlur(img, ksize=(5,5), sigmaX=0)
edged = cv2.Canny(blur, 10, 250)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
contours, _ = cv2.findContours(closed.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
total = 0
contours_image = cv2.drawContours(img, contours, -1, (0,255,0), 3)


cv2.imshow('contours_image', contours_image)
cv2.waitKey()
cv2.destroyAllWindows()         