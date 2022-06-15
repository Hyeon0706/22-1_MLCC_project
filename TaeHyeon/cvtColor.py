import glob
import cv2
img_files = glob.glob('D:\MLCC_Image\P052012235019(NSW528)\error_mlcc/*tif') # 정상 이미지 경로
# img_files = glob.glob('D:\MLCC_Image\errorimg/*tif') # 불량 이미지 경로

i=1
for path in img_files:
    print(path)
    img = cv2.imread(path)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    
    ret, all = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY) # 전체를 흰색으로 이진화

    contours_all, hierarchy = cv2.findContours(all, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # 전체 윤곽선 검출
    
    x,y,width,height=0,0,0,0
    for cnt in contours_all:
        if cv2.contourArea(cnt)>10000: # 잘못 설정되는 값을 제외하기 위해 면적이 10000보다 크면 사각형 그림
            x, y, width, height = cv2.boundingRect(cnt)
    cropped = gray[y:y+height, x:x+width]
    dst = cv2.resize(cropped, dsize=(210, 105), interpolation=cv2.INTER_AREA)
    # 좌우대칭
    fh = cv2.flip(dst, 1)
    # 상하대칭
    fv = cv2.flip(dst, 0)
    # 좌우&상하대칭
    fb = cv2.flip(dst, -1)
            
    
    # cv2.imwrite('D:\MLCC_Image\/new_error\gray-%d.jpg'%i,dst)
    # cv2.imwrite('D:\MLCC_Image\P052012235019(NSW528)\/train_normal/flip1-%d.jpg'%i,fh)
    # cv2.imwrite('D:\MLCC_Image\P052012235019(NSW528)\/train_normal/flip2-%d.jpg'%i,fv)
    # cv2.imwrite('D:\MLCC_Image\P052012235019(NSW528)\/train_normal/flip3-%d.jpg'%i,fb)
    
    # cv2.imwrite('D:\MLCC_Image\/new_normal\gray-%d.jpg'%i,dst)
    cv2.imwrite('D:\MLCC_Image\P052012235019(NSW528)\/train_error/flip1-%d.jpg'%i,fh)
    cv2.imwrite('D:\MLCC_Image\P052012235019(NSW528)\/train_error/flip2-%d.jpg'%i,fv)
    cv2.imwrite('D:\MLCC_Image\P052012235019(NSW528)\/train_error/flip3-%d.jpg'%i,fb)
    i+=1