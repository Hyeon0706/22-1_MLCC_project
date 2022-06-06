import cv2
def contour(src):
    target_img = src.copy() # 사본 이미지

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    ret, all = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY) # 전체를 흰색으로 이진화

    contours_all, hierarchy = cv2.findContours(all, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # 전체 윤곽선 검출
    
    size=[]
    x,y,width,height=0,0,0,0
    for cnt in contours_all:
        if cv2.contourArea(cnt)>10000: # 잘못 설정되는 값을 제외하기 위해 면적이 10000보다 크면 사각형 그림
            x, y, width, height = cv2.boundingRect(cnt)
            # cv2.rectangle(target_img, (x, y), (x + width, y + height), Green, 2) # 전체 사각형 그리기
            print(cv2.contourArea(cnt)) # 검출된 면적 출력
            size.append(cv2.contourArea(cnt))
            cv2.imshow('win',target_img)
            cropped = target_img[y:y+height, x:x+width]
            cv2.imshow('crop',cropped)
            print(cropped.shape)
            dst = cv2.resize(cropped, dsize=(210, 105), interpolation=cv2.INTER_AREA)
            cv2.imshow('dst',dst)
            print(dst.shape)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    
img = cv2.imread('D:\MLCC_Image\P052012235019(NSW528)\/007-1.tif')
contour(img)