import cv2
import numpy as np
def contour(src):
    target_img = src.copy() # 사본 이미지

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) #윤곽선 검출
    # 윤곽선 정보, 구조
    # 이미지, 윤곽선 찾는 모드 (mode), 윤곽선 찾을때 사용하는 근사치 방법 (method)

    COLOR =  (0, 200, 0) # 녹색
    cv2.drawContours(target_img, contours, -1, COLOR, 2) # 윤곽선 그리기
    # 대상 이미지, 윤곽선 정보, 인덱스 값 (-1 : 전체 윤곽선), 색, 두께


    cv2.imshow('contour',target_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
img=cv2.imread('001-1.tif')
contour(img)