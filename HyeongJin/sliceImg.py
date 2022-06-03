import cv2
import numpy as np

def get_sliceImg(image_origin):
    margin = -15  
    image_copy = image_origin.copy()
    imgray = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)

    #전극부분 이진화
    ret, thr = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY) 
    contours, _ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #바디부분 이진화
    ret_body, thr_body = cv2.threshold(imgray, 127, 255, cv2.THRESH_TOZERO_INV) 
    _body, binary_body = cv2.threshold(thr_body,50,255,cv2.THRESH_BINARY)
    se = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    ope = cv2.morphologyEx(binary_body, cv2.MORPH_OPEN, se)
    contours_body, _ = cv2.findContours(ope, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    origin_height, origin_width = image_copy.shape[:2]  
    crop_images = []  # 전극 이미지를 추가할 리스트
    body_image = []   # 바디 이미지를 추가할 리스트

    for contour in contours: #전극 좌표값
        x, y, width, height = cv2.boundingRect(contour)  # 좌상단 꼭지점 좌표 , width, height

        # 전극의 size 가 기준 이상인 것만 담는다.
        if width > 20 and height > 80:
            crop_row_1 = (y - margin) if (y - margin) > 0 else y
            crop_row_2 = (y + height + margin) if (y + height + margin) < origin_height else y + height
            crop_col_1 = (x - margin) if (x - margin) > 0 else x
            crop_col_2 = (x + width + margin) if (x + width + margin) < origin_width else x + width

            
            crop = image_copy[crop_row_1: crop_row_2, crop_col_1: crop_col_2]  # 이미지를 잘라낸다.
            crop_images.append(crop)  # 잘라낸 이미지들을 하나씩 리스트에 담는다.

    for contour_body in contours_body: #바디 좌표값
        x, y, width, height = cv2.boundingRect(contour_body)  # 좌상단 꼭지점 좌표 , width, height

        # 바디의 size 가 기준 이상인 것만 담는다.
        if width > 20 and height > 80:
            crop_row_1_body = (y - margin) if (y - margin) > 0 else y
            crop_row_2_body = (y + height + margin) if (y + height + margin) < origin_height else y + height
            crop_col_1_body = (x - margin) if (x - margin) > 0 else x
            crop_col_2_body = (x + width + margin) if (x + width + margin) < origin_width else x + width

           
            crop_body = image_copy[crop_row_1_body: crop_row_2_body, crop_col_1_body: crop_col_2_body]  # 이미지를 잘라낸다.
            body_image.append(crop_body)  # 잘라낸 이미지들을 하나씩 리스트에 담는다.        

    # slice1 = cv2.resize(crop_images[0], dsize=(200, 488), interpolation=cv2.INTER_AREA) #전극 크기 조절해서 자르기.
    # slice2 = cv2.resize(crop_images[1], dsize=(200, 488), interpolation=cv2.INTER_AREA)
    cv2.imshow('e1',crop_images[0])
    cv2.imshow('e2',crop_images[1])
    cv2.imshow('body',body_image[0])
    
    return crop_images[0], crop_images[1], body_image[0]