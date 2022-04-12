import cv2
import numpy as np
def contour(src):
    target_img = src.copy() # 사본 이미지

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    ret, electrode = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY) # 전극만 흰색으로 이진화
    ret, all = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # 전체를 흰색으로 이진화

    contours_all, hierarchy = cv2.findContours(all, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # 전체 윤곽선 검출
    contours_electrode, hierarchy = cv2.findContours(electrode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # 전극 윤곽선 검출
    # 윤곽선 정보, 구조
    # 이미지, 윤곽선 찾는 모드 (mode), 윤곽선 찾을때 사용하는 근사치 방법 (method)

    Green = (0,200,0) # 녹색
    Red = (0,0,200) # 붉은색
    
    for cnt in contours_all:
        x, y, width, height = cv2.boundingRect(cnt)
        cv2.rectangle(target_img, (x, y), (x + width, y + height), Green, 2) # 사각형 그리기
        
    for cnt in contours_electrode:
        x, y, width, height = cv2.boundingRect(cnt)
        cv2.rectangle(target_img, (x, y), (x + width, y + height), Red, 2) # 사각형 그리기


    cv2.imshow('contour',target_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
img=cv2.imread('001-1.tif')
contour(img)