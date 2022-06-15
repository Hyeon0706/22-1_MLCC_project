import cv2
import numpy as np

def check_color(left_side, right_side, middle_side):
    result = 1
    th = 90          #이진화 임계값
    thb = 170    
    side_px = 3060  # 픽셀수 한계값
    body_px = 2550 
    
    
    left_gray = cv2.cvtColor(left_side, cv2.COLOR_BGR2GRAY)
    right_gray = cv2.cvtColor(right_side, cv2.COLOR_BGR2GRAY)
    middle_gray = cv2.cvtColor(middle_side, cv2.COLOR_BGR2GRAY)
    
    ret, bin1 = cv2.threshold(left_gray,th,255,cv2.THRESH_BINARY_INV)
    ret, bin2 = cv2.threshold(right_gray,th,255,cv2.THRESH_BINARY_INV)
    ret, bin3 = cv2.threshold(middle_gray,thb,255,cv2.THRESH_BINARY)

    count1 = np.sum(bin1)
    count2 = np.sum(bin2)
    count3 = np.sum(bin3)
    
    # if count1 < count2 :
    #     count1 = count2
    
    if count1 > side_px  or count2 > side_px:
        print('error in electrode brightness')
        return 1
    
    if count3 > body_px :
        print('error in body brightness')
        return 1