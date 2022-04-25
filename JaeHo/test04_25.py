import cv2
import numpy as np

def contour():

    img = cv2.imread('001-1.tif')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thr = cv2.threshold(imgray, 50, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

   
    max = 0
    maxcnt = None

    for cnt in contours :
            area = cv2.contourArea(cnt)
            if(max < area) :
                max = area
                maxcnt = cnt

    hull = cv2.convexHull(maxcnt)
    mask = np.zeros(img.shape).astype(img.dtype)
    color = [255, 255, 255]
    cv2.fillPoly(mask, [maxcnt], color)

    img_mlcc = cv2.bitwise_and(img, mask)



    cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
    cv2.drawContours(img_mlcc, [maxcnt],-1, (255,0,0), 3)
    cv2.drawContours(img_mlcc, [hull],-1, (0,255,0), 3)
    

  

    cv2.imshow('image', img_mlcc)
    cv2.imshow('thr', thr)
    cv2.imshow('contours', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


contour()
