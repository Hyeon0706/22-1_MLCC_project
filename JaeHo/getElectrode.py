import cv2
import numpy as np

def get_electrode1(image_origin):
    margin = -8  # 원하는 margin
    image_copy = image_origin.copy()
    imgray = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
    ret, thr = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    origin_height, origin_width = image_copy.shape[:2]  # get image size
    crop_images = []  # 자른 이미지를 하나씩 추가해서 저장할 리스트

    for contour in contours:
        x, y, width, height = cv2.boundingRect(contour)  # 좌상단 꼭지점 좌표 , width, height

        # Rect 의 size 가 기준 이상인 것만 담는다
        if width > 20 and height > 80:
            crop_row_1 = (y - margin) if (y - margin) > 0 else y
            crop_row_2 = (y + height + margin) if (y + height + margin) < origin_height else y + height
            crop_col_1 = (x - margin) if (x - margin) > 0 else x
            crop_col_2 = (x + width + margin) if (x + width + margin) < origin_width else x + width

            
            crop = image_copy[crop_row_1: crop_row_2, crop_col_1: crop_col_2]  # 이미지를 잘라낸다.
            crop_images.append(crop)  # 잘라낸 이미지들을 하나씩 리스트에 담는다.

    slice1 = cv2.resize(crop_images[0], dsize=(200, 488), interpolation=cv2.INTER_AREA)
    return slice1

def get_electrode2(image_origin):
    margin = -8  # 원하는 margin
    image_copy = image_origin.copy()
    imgray = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
    ret, thr = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    origin_height, origin_width = image_copy.shape[:2] 
    crop_images = []  # 자른 이미지를 하나씩 추가해서 저장할 리스트

    for contour in contours:
        x, y, width, height = cv2.boundingRect(contour)  # 좌상단 꼭지점 좌표 , width, height

        # Rect 의 size 가 기준 이상인 것만 담는다
        if width > 20 and height > 80:
            crop_row_1 = (y - margin) if (y - margin) > 0 else y
            crop_row_2 = (y + height + margin) if (y + height + margin) < origin_height else y + height
            crop_col_1 = (x - margin) if (x - margin) > 0 else x
            crop_col_2 = (x + width + margin) if (x + width + margin) < origin_width else x + width

           
            crop = image_copy[crop_row_1: crop_row_2, crop_col_1: crop_col_2]  # 이미지를 잘라낸다.
            crop_images.append(crop)  # 잘라낸 이미지들을 하나씩 리스트에 담는다.

    slice2 = cv2.resize(crop_images[1], dsize=(200, 488), interpolation=cv2.INTER_AREA)
    return slice2

#테스트 용.
img = cv2.imread('C:\/finalProject\JaeHo\/160-3.tif')


cv2.imshow('image1', get_electrode1(img))
cv2.imshow('image2', get_electrode2(img))
cv2.waitKey(0)
cv2.destroyAllWindows()



