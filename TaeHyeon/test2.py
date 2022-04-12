import cv2

img=cv2.imread('D:\MLCC_Image\외관 검사용 이미지\/3216 SIZE\OkImage\P052012235019(NSW528)\/001-1.tif')
cv2.imshow('win',img)

cv2.waitKey(0)
cv2.destroyAllWindows()