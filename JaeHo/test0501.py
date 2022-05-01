import cv2

src = cv2.imread('001-1.tif')

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(src, [contours[0]], 0, (0, 0, 255), 2)
cv2.imshow("src", src)
cv2.waitKey(0)


cv2.destroyAllWindows()