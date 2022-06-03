import cv2

def check_color(left_side, right_side, middle_side):
    result = True
    left_count = 0
    right_count = 0
    middle_count = 0
    th = 250    #이진화 임계값
    px = 1000    # 픽셀수 한계값
    
    
    left_gray = cv2.cvtColor(left_side, cv2.COLOR_BGR2GRAY)
    right_gray = cv2.cvtColor(right_side, cv2.COLOR_BGR2GRAY)
    middle_gray = cv2.cvtColor(middle_side, cv2.COLOR_BGR2GRAY)
    
    left_gray = cv2.inRange(left_gray, th, 255)
    right_gray = cv2.inRange(right_gray, th, 255)
    middle_gray = cv2.inRange(middle_gray, th, 255)
    
    
    for iii in range(len(left_gray)):
        for jjj in range(len(left_gray[iii])):
            if left_gray[iii][jjj] != 0:
                left_count += 1
        
    for iii in range(len(right_gray)):
        for jjj in range(len(right_gray[iii])):
            if right_gray[iii][jjj] != 0:
                right_count += 1
                
    for iii in range(len(middle_gray)):
        for jjj in range(len(middle_gray[iii])):
            if middle_gray[iii][jjj] != 0:
                middle_count += 1       
                                    
    if (left_count >= px) or (right_count >= px):
        result = False
    
    if (middle_count >= 0):
        result = False
    print('result : ',result)
    return result