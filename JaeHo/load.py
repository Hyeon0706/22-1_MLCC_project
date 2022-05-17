import cv2
import numpy as np


def sliceEle1(src) : #전극1
    target_img = src.copy()

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    ret, electrode = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours_electrode, hierarchy = cv2.findContours(electrode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours_xy = np.array([contours_electrode[0]])
    
    # x의 min과 max 찾기
    x_min, x_max = 0,0
    value = list()
    for i in range(len(contours_xy)):
        for j in range(len(contours_xy[i])):
            value.append(contours_xy[i][j][0][0]) #네번째 괄호가 0일때 x의 값
            x_min = min(value)
            x_max = max(value)
   
    
    # y의 min과 max 찾기
    y_min, y_max = 0,0
    value = list()
    for i in range(len(contours_xy)):
        for j in range(len(contours_xy[i])):
            value.append(contours_xy[i][j][0][1]) #네번째 괄호가 0일때 x의 값
            y_min = min(value)
            y_max = max(value)
    
    x = x_min
    y = y_min
    w = x_max-x_min
    h = y_max-y_min
    
    right_electrode = target_img[y:y+h, x:x+w]
    return right_electrode



def sliceEle2(src) : #전극2
    target_img = src.copy()

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    ret, electrode = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours_electrode, hierarchy = cv2.findContours(electrode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours_xy = np.array([contours_electrode[1]])
    
    # x의 min과 max 찾기
    x_min, x_max = 0,0
    value = list()
    for i in range(len(contours_xy)):
        for j in range(len(contours_xy[i])):
            value.append(contours_xy[i][j][0][0]) #네번째 괄호가 0일때 x의 값
            x_min = min(value)
            x_max = max(value)
   
    
    # y의 min과 max 찾기
    y_min, y_max = 0,0
    value = list()
    for i in range(len(contours_xy)):
        for j in range(len(contours_xy[i])):
            value.append(contours_xy[i][j][0][1]) #네번째 괄호가 0일때 x의 값
            y_min = min(value)
            y_max = max(value)
    
    x = x_min
    y = y_min
    w = x_max-x_min
    h = y_max-y_min
    
    left_electrode = target_img[y:y+h, x:x+w]
    return left_electrode