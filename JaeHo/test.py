import cv2


def empty(pos):
    #     print(pos)
    pass

img = cv2.imread('001-1.tif',cv2.IMREAD_GRAYSCALE)

name = 'Trackbar'
cv2.namedWindow(name)

cv2.createTrackbar('threshold',name,127,255,empty) # bar 이름, 창의 이름, 초기값, 최대값, 이벤트 처리

while 1:
    thresh = cv2.getTrackbarPos('threshold',name) # bar 이름, 창의 이름
    ret, binary_toz = cv2.threshold(img,thresh,255,cv2.THRESH_TOZERO_INV) # tozero_inv 로 전극 부분 검은색으로 만든 다음
    _, binary = cv2.threshold(binary_toz,50,255,cv2.THRESH_BINARY) # 위 이미지를 이진화
    se = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5)) # 이진화만 하면 테두리가 그대로 남아있어서
    ope = cv2.morphologyEx(binary, cv2.MORPH_OPEN, se) # 열림 연산을 통해 노이즈 제거
    if not ret:
        break
        
    cv2.imshow(name,ope)
    if cv2.waitKey(1) == ord('q'):
        break
    


