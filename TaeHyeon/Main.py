import tkinter
import cv2
from PIL import Image
from PIL import ImageTk
import Contour # Contour.py 를 import 하여 contour()함수를 사용

cnt=0

def click(): # 버튼 이벤트는 이렇게 함수로 만들어서 사용하면 됨
    global cnt
    cnt+=1
    result.config(text="오류 개수 : " + str(cnt))
    check_size.config(bg='blue')

window=tkinter.Tk()
window.title('MLCC Scanner') # 윈도우 이름
window.geometry('840x300+100+100') # 윈도우 사이즈
window.resizable(0, 0) # 크기조절 => False,0이면 사이즈 조절 불가

src=cv2.imread('001-1.tif')
# test.read(src)
# Contour.contour(src)
img=cv2.cvtColor(src,cv2.COLOR_BGR2RGB)

# 이렇게 해야 tif 파일이 읽히는듯...
img=Image.fromarray(img)
imgtk=ImageTk.PhotoImage(image=img)

# 각 위젯별 형태
label=tkinter.Label(window, image=imgtk)
result=tkinter.Label(window, text="오류 개수 : " + str(cnt),bg='gray')
check_size=tkinter.Label(window, text="크기 검사대기",bg='gray')
check_color=tkinter.Label(window, text="이물질 검사대기",bg='gray')
check_line=tkinter.Label(window, text="라인 검사대기",bg='gray')
b_back=tkinter.Button(window,text='이전')
b_next=tkinter.Button(window,text='다음',command=click)


# 각 위젯별 위치
label.place(x=0,y=0)
result.place(x=0,y=250,width=640,height=40)
check_size.place(x=650,y=10,width=180,height=70)
check_color.place(x=650,y=90,width=180,height=70)
check_line.place(x=650,y=170,width=180,height=70)
b_back.place(x=650,y=250,width=85,height=40)
b_next.place(x=745,y=250,width=85,height=40)

window.mainloop()