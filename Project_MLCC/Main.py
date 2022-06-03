import tkinter
import cv2
from PIL import Image
from PIL import ImageTk
import Contour
import sliceImg as si # 이미지 영역 설정
import checkBright as cb # 이미지 밝기 검사
import glob

cnt=0
page=-1
img_path=''
cut_img=[]

def next_click(): # 다음 버튼
    global page
    global img_path
    global cut_img
    page+=1 # 다음 이미지를 로드하기 위해 page+=1
    check_size.config(bg='blue')
    src = cv2.imread(img_files[page])
    print(img_files[page])
    img=cv2.cvtColor(src,cv2.COLOR_BGR2RGB)
    img=Image.fromarray(img)
    imgtk=ImageTk.PhotoImage(image=img)
    print(imgtk)
    img_path = imgtk
    label.config(image=imgtk)
    if scan_size(src)==0:
        e1, e2, body = si.get_sliceImg(src) # 로드한 이미지 파일을 이미지 영역 설정 함수로 넘김
        cb.check_color(e1,e2,body)
        
def back_click(): # 이전 버튼
    global page
    global img_path
    page-=1
    check_size.config(bg='blue')
    src = cv2.imread(img_files[page])
    si.get_sliceImg(src) # 로드한 이미지 파일을 이미지 영역 설정 함수로 넘김
    print(img_files[page])
    img=cv2.cvtColor(src,cv2.COLOR_BGR2RGB)
    img=Image.fromarray(img)
    imgtk=ImageTk.PhotoImage(image=img)
    print(imgtk)
    img_path = imgtk
    label.config(image=imgtk)
    scan_size(src)
    
def auto_click(): # 자동 버튼
    global page
    global img_path
    for i in range(page,len(img_files)):
        page+=1
        src = cv2.imread(img_files[i])
        si.get_sliceImg(src) # 로드한 이미지 파일을 이미지 영역 설정 함수로 넘김
        print(img_files[i])
        img=cv2.cvtColor(src,cv2.COLOR_BGR2RGB)
        img=Image.fromarray(img)
        imgtk=ImageTk.PhotoImage(image=img)
        print(imgtk)
        img_path = imgtk
        label.config(image=imgtk)
        if scan_size(src) == 1: # 에러를 발견하면 멈춘 후 보여줌
            break
    
def scan_size(src): # 사이즈 검사
    global cnt
    error = Contour.contour(src)
    if error : # 만약 에러가 검출되면
        cnt+=1 # 검사 결과값에 +=1
        result.config(text="오류 개수 : " + str(cnt))
        check_size.config(bg='red') # 크기검사 영역 붉은색
        return 1
    else:
        check_size.config(bg='blue') # 크기검사 영역 파란색
        return 0
    
window=tkinter.Tk()
window.title('MLCC Scanner') # 윈도우 이름
window.geometry('840x350+100+100') # 윈도우 사이즈
window.resizable(0, 0) # 크기조절 => False,0이면 사이즈 조절 불가

img_files = glob.glob('D:\MLCC_Image\P052012235019(NSW528)/*tif') # glob 라이브러리 이용해서 이미지 여러장 로드

# 각 위젯별 형태
label=tkinter.Label(window, image=img_path)
result=tkinter.Label(window, text="오류 개수 : " + str(cnt),bg='gray')
check_size=tkinter.Label(window, text="크기 검사",bg='gray')
check_color=tkinter.Label(window, text="이물질 검사",bg='gray')
check_line=tkinter.Label(window, text="라인 검사",bg='gray')
b_back=tkinter.Button(window,text='이전',command=back_click)
b_next=tkinter.Button(window,text='다음',command=next_click)
b_auto=tkinter.Button(window,text='자동 검사',command=auto_click)


# 각 위젯별 위치
label.place(x=0,y=0)
result.place(x=0,y=250,width=640,height=40)
check_size.place(x=650,y=10,width=180,height=70)
check_color.place(x=650,y=90,width=180,height=70)
check_line.place(x=650,y=170,width=180,height=70)
b_back.place(x=650,y=250,width=85,height=40)
b_next.place(x=745,y=250,width=85,height=40)
b_auto.place(x=650,y=300,width=180,height=40)

window.mainloop()