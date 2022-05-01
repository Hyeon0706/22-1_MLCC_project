import tkinter
import cv2
from PIL import Image
from PIL import ImageTk
import Contour # Contour.py 를 import 하여 contour()함수를 사용
import glob

cnt=0
page=0
img_path=''

def next_click(): # 버튼 이벤트는 이렇게 함수로 만들어서 사용하면 됨
    global page
    global img_path
    check_size.config(bg='blue')
    src = cv2.imread(img_files[page])
    print(img_files[page])
    img=cv2.cvtColor(src,cv2.COLOR_BGR2RGB)
    img=Image.fromarray(img)
    imgtk=ImageTk.PhotoImage(image=img)
    print(imgtk)
    img_path = imgtk
    label.config(image=imgtk)
    chekc_size(src)
    page+=1 # 다음 이미지를 로드하기 위해 page+=1
    
def chekc_size(src): # 사이즈 검사
    global cnt
    error = Contour.contour(src)
    if error : # 만약 에러가 검출되면
        cnt+=1 # 검사 결과값에 +=1
        result.config(text="오류 개수 : " + str(cnt))
        check_size.config(bg='red') # 크기검사 영역 붉은색
    else:
        check_size.config(bg='blue') # 크기검사 영역 파란색
window=tkinter.Tk()
window.title('MLCC Scanner') # 윈도우 이름
window.geometry('840x300+100+100') # 윈도우 사이즈
window.resizable(0, 0) # 크기조절 => False,0이면 사이즈 조절 불가

img_files = glob.glob('D:\MLCC_Image\P052012235019(NSW528)/*tif') # glob 라이브러리 이용해서 이미지 여러장 로드

# 각 위젯별 형태
label=tkinter.Label(window, image=img_path)
result=tkinter.Label(window, text="오류 개수 : " + str(cnt),bg='gray')
check_size=tkinter.Label(window, text="크기 검사대기",bg='gray')
check_color=tkinter.Label(window, text="이물질 검사대기",bg='gray')
check_line=tkinter.Label(window, text="라인 검사대기",bg='gray')
b_back=tkinter.Button(window,text='이전')
b_next=tkinter.Button(window,text='다음',command=next_click)


# 각 위젯별 위치
label.place(x=0,y=0)
result.place(x=0,y=250,width=640,height=40)
check_size.place(x=650,y=10,width=180,height=70)
check_color.place(x=650,y=90,width=180,height=70)
check_line.place(x=650,y=170,width=180,height=70)
b_back.place(x=650,y=250,width=85,height=40)
b_next.place(x=745,y=250,width=85,height=40)

window.mainloop()