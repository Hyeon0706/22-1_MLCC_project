import cv2
def contour(src):
    target_img = src.copy() # 사본 이미지

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    ret, electrode = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY) # 전극만 흰색으로 이진화
    ret, all = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY) # 전체를 흰색으로 이진화

    contours_all, hierarchy = cv2.findContours(all, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # 전체 윤곽선 검출
    contours_electrode, hierarchy = cv2.findContours(electrode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # 전극 윤곽선 검출
    # 윤곽선 정보, 구조
    # 이미지, 윤곽선 찾는 모드 (mode), 윤곽선 찾을때 사용하는 근사치 방법 (method)

    Green = (0,200,0) # 녹색(전체)
    Red = (0,0,200) # 붉은색(전극)
    
    size=[]
    
    for cnt in contours_all:
        if cv2.contourArea(cnt)>10000: # 잘못 설정되는 값을 제외하기 위해 면적이 10000보다 크면 사각형 그림
            x, y, width, height = cv2.boundingRect(cnt)
            cv2.rectangle(target_img, (x, y), (x + width, y + height), Green, 2) # 전체 사각형 그리기
            # print(cv2.contourArea(cnt)) # 검출된 면적 출력
            size.append(cv2.contourArea(cnt))
            if cv2.contourArea(cnt) < 19100 or cv2.contourArea(cnt) > 21750:
                print('error in all')
                return 1
            else:
                print('no error in all')
        
    for cnt in contours_electrode:
        if cv2.contourArea(cnt)>3000:
            x, y, width, height = cv2.boundingRect(cnt)
            cv2.rectangle(target_img, (x, y), (x + width, y + height), Red, 2) # 전극 사각형 그리기
            # print(cv2.contourArea(cnt)) # 검출된 면적 출력
            size.append(cv2.contourArea(cnt))
            if cv2.contourArea(cnt) < 3086 or cv2.contourArea(cnt) > 3978:
                print('error in electrode')
                return 1
            else:
                print('no error in electrode')
    # print(size)

    if len(size) != 3:
        print('error')
        return 1