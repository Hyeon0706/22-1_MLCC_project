# 이미지의 이진화 오류를 해결하기 위해 작성
import cv2

def empty(pos):
#     print(pos)
    pass

img = cv2.imread('D:\MLCC_Image\P052012235019(NSW528)\/005-3.tif',cv2.IMREAD_GRAYSCALE)

name = 'Trackbar'
cv2.namedWindow(name)

cv2.createTrackbar('threshold',name,127,255,empty) # bar 이름, 창의 이름, 초기값, 최대값, 이벤트 처리

while 1:
    thresh = cv2.getTrackbarPos('threshold',name) # bar 이름, 창의 이름
    ret, binary = cv2.threshold(img,thresh,255,cv2.THRESH_BINARY)
    
    if not ret:
        break
        
    cv2.imshow(name,binary)
    if cv2.waitKey(1) == ord('q'):
        break
    
cv2.destroyAllWindows()