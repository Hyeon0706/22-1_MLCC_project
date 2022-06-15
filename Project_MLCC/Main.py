import tkinter
import cv2
from PIL import Image
from PIL import ImageTk
import checkSize as cs
import sliceImg as si # 이미지 영역 설정
import UseAI as ua # AI
import checkBright as cb # 밝기 검사
import glob
import tkinter.ttk as ttk
from datetime import datetime
from tkinter import DoubleVar, filedialog


page=-1
img_path=''
cut_img=[]
is_on = False
cnt=0

def next_click(): # 다음 버튼
    global page
    global img_path
    global cut_img
    global cnt
    page+=1 # 다음 이미지를 로드하기 위해 page+=1
    check_size.config(bg='blue')
    src = cv2.imread(img_files[page])
    img1,img2,img3 = si.get_sliceImg(src) # 로드한 이미지 파일을 이미지 영역 설정 함수로 넘김
    print(img_files[page])
    img=cv2.cvtColor(src,cv2.COLOR_BGR2RGB)
    img=Image.fromarray(img)
    imgtk=ImageTk.PhotoImage(image=img)
    print(imgtk)
    img_path = imgtk
    label.config(image=imgtk)
    size_state = scan_size(src)
    bright_state = scan_bright(img1,img2,img3)
    now = datetime.now()
    ai_state = 1
    res = ''
    if is_on:
        ai_state = ua.checkAi(src)
    if size_state == 1 or ai_state == 0 or bright_state == 1:
        res = 'error'
        cnt+=1
        result.configure(text='불량 개수 : ' + str(cnt))
    else:
        res = 'normal'
    time = now.strftime('%Y-%m-%d %H:%M:%S') +'  ' + img_files[page] + '  ' + res
    list.insert(tkinter.END, time)
    
def back_click(): # 이전 버튼
    global page
    global img_path
    page-=1
    check_size.config(bg='blue')
    src = cv2.imread(img_files[page])
    img1,img2,img3 = si.get_sliceImg(src) # 로드한 이미지 파일을 이미지 영역 설정 함수로 넘김
    print(img_files[page])
    img=cv2.cvtColor(src,cv2.COLOR_BGR2RGB)
    img=Image.fromarray(img)
    imgtk=ImageTk.PhotoImage(image=img)
    print(imgtk)
    img_path = imgtk
    label.config(image=imgtk)
    size_state = scan_size(src)
    bright_state = scan_bright(img1,img2,img3)
    now = datetime.now()
    ai_state = 1
    res = ''
    if is_on:
        ai_state = ua.checkAi(src)
    if size_state == 1 or ai_state == 0 or bright_state == 1:
        res = 'error'
    else:
        res = 'normal'
    time = now.strftime('%Y-%m-%d %H:%M:%S') +'  ' + img_files[page] + '  ' + res
    list.insert(tkinter.END, time)

    
def auto_click(): # 자동 버튼
    global page
    global img_path
    global cnt
    for i in range(page,len(img_files)):
        page+=1
        p_var.set(i)
        progressbar.update()
        src = cv2.imread(img_files[i])
        img1,img2,img3 = si.get_sliceImg(src) # 로드한 이미지 파일을 이미지 영역 설정 함수로 넘김
        print(img_files[i])
        img=cv2.cvtColor(src,cv2.COLOR_BGR2RGB)
        img=Image.fromarray(img)
        imgtk=ImageTk.PhotoImage(image=img)
        print(imgtk)
        img_path = imgtk
        label.config(image=imgtk)
        size_state = scan_size(src)
        bright_state = scan_bright(img1,img2,img3)
        now = datetime.now()
        ai_state = 1
        if is_on:
            ai_state = ua.checkAi(src)
        if size_state == 1 or ai_state == 0 or bright_state == 1:
            time = now.strftime('%Y-%m-%d %H:%M:%S') +'  ' + img_files[page-1] + '  ' + 'error'
            list.insert(tkinter.END, time)
            cnt+=1
            result.configure(text='불량 개수 : ' + str(cnt))
        else:
            time = now.strftime('%Y-%m-%d %H:%M:%S') +'  ' + img_files[page-1] + '  ' + 'normal'
            list.insert(tkinter.END, time)
    
def scan_size(src): # 사이즈 검사
    error = cs.contour(src)
    if error : # 만약 에러가 검출되면
        check_size.config(bg='red') # 크기검사 영역 붉은색
        return 1
    else:
        check_size.config(bg='blue') # 크기검사 영역 파란색
        
def scan_bright(img1,img2,img3):
    error = cb.check_color(img1,img2,img3)
    if error : # 만약 에러가 검출되면
        check_color.config(bg='red') # 밝기검사 영역 붉은색
        return 1
    else:
        check_color.config(bg='blue') # 밝기검사 영역 파란색     
           
def switch():
    global is_on
     
    # Determine is on or off
    if is_on:
        on_button.config(image = off)
        check_AI.config(bg='gray') # 크기검사 영역 붉은색
        is_on = False
    else:
       
        on_button.config(image = on)
        check_AI.config(bg='blue') # 크기검사 영역 붉은색
        is_on = True

def checkImg():
    global img_path
    a = list.get(list.curselection()[0])
    split_a = a.split('  ')
    src = cv2.imread(split_a[1])
    si.get_sliceImg(src) # 로드한 이미지 파일을 이미지 영역 설정 함수로 넘김
    img=cv2.cvtColor(src,cv2.COLOR_BGR2RGB)
    img=Image.fromarray(img)
    imgtk=ImageTk.PhotoImage(image=img)
    img_path = imgtk
    label.config(image=imgtk)
    
def close_window():
    window.destroy()
    

window=tkinter.Tk()
window.title('MLCC Scanner') # 윈도우 이름
window.geometry('840x700+100+100') # 윈도우 사이즈
window.resizable(0, 0) # 크기조절 => False,0이면 사이즈 조절 불가

filename = filedialog.askdirectory()
print(filename)

on = tkinter.PhotoImage(file = "Project_MLCC\on.png")
off = tkinter.PhotoImage(file = "Project_MLCC\off.png")

img_files = glob.glob(filename + '/*tif') # glob 라이브러리 이용해서 이미지 여러장 로드

# 각 위젯별 형태
label=tkinter.Label(window, image=img_path)
check_size=tkinter.Label(window, text="크기 검사",bg='gray')
check_color=tkinter.Label(window, text="밝기 검사",bg='gray')
check_AI=tkinter.Label(window, text="AI 검사",bg='gray')
filepath=tkinter.Label(window, text="파일 경로 : " + filename,bg='white')
result=tkinter.Label(window, text="불량 개수 : 0",bg='white')
b_back=tkinter.Button(window,text='이전',command=back_click)
b_next=tkinter.Button(window,text='다음',command=next_click)
b_auto=tkinter.Button(window,text='자동 검사',command=auto_click)
check_img=tkinter.Button(window,text='확인',command=checkImg)
close=tkinter.Button(window,text='종료',command=close_window)
on_button = tkinter.Button(window, image = off, bd = 0,command = switch)
frame = tkinter.Frame(window)
frame.pack()

scrollbar = tkinter.Scrollbar(frame)
scrollbar.pack(side='right',fill='y')
list = tkinter.Listbox(frame, selectmode="extended", width = 800, height=300, yscrollcommand = scrollbar.set)
list.pack(side='left')

p_var = DoubleVar()
progressbar = ttk.Progressbar(window,maximum=len(img_files),length=640,variable=p_var)
progressbar.pack()

# 각 위젯별 위치
label.place(x=0,y=0)
check_size.place(x=650,y=10,width=180,height=70)
check_color.place(x=650,y=90,width=180,height=70)
check_AI.place(x=650,y=170,width=80,height=70)
filepath.place(x=0,y=250,width=500,height=40)
result.place(x=510,y=250,width=130,height=40)
b_back.place(x=650,y=250,width=85,height=40)
b_next.place(x=745,y=250,width=85,height=40)
b_auto.place(x=650,y=300,width=180,height=40)
check_img.place(x=0,y=660,width=180,height=40)
close.place(x=650,y=660,width=180,height=40)
on_button.place(x=740,y=180,width=100,height=40)
frame.place(x=0,y=350,width=840,height=300)
progressbar.place(x=0,y=320)

window.mainloop()