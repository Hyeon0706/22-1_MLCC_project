import tensorflow as tf
import cv2
import numpy as np

def checkAi(src):
    test_img=[]
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    ret, all = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY) # 전체를 흰색으로 이진화

    contours_all, hierarchy = cv2.findContours(all, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # 전체 윤곽선 검출
    
    x,y,width,height=0,0,0,0
    for cnt in contours_all:
        if cv2.contourArea(cnt)>10000: # 잘못 설정되는 값을 제외하기 위해 면적이 10000보다 크면 사각형 그림
            x, y, width, height = cv2.boundingRect(cnt)
    cropped = gray[y:y+height, x:x+width]
    dst = cv2.resize(cropped, dsize=(210, 105), interpolation=cv2.INTER_AREA)
    
    test_img.append(dst)

    test_img=np.array(test_img)
    test_img = test_img/255.0

    test_img = test_img.reshape(test_img.shape[0],test_img.shape[1]*test_img.shape[2])

    loaded_model = tf.keras.models.load_model('Project_MLCC\model_2.h5')

    pred = loaded_model.predict(test_img)
    if pred[0][0] > pred[0][1]:
        print('AI error')
        return 0 # error
    else:
        print('AI normal')
        return 1 # normal