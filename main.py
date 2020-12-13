'''
這邊是寫 GUI 的介面，動作的部分是寫在 Gfunction.py
GUI 的部分用的是 class的概念 和 tkinter
想要新增什麼樣的元件，方式很簡單。
def __init__ 去新增就可以了，

寫成函數的方式比較明瞭，所以大家加油吧，首先你要讀懂他在寫什麼。

最後是上傳的時候，不要有錯誤讓沒辦法跑

方式 :
git add <file>
git commit -m "<message>"
git push

記得在修改之前先打

git pull
'''
import tkinter as tk
from tkinter import  ttk

from Gfunction import GUI_Function


class Root(GUI_Function  ,tk.Frame ):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        
        #entry=tk.Entry(RootWindow,insertbackground='blue', highlightthickness =2)#用來參考的程式碼
        #canvas.create_window(256,174, width=100, height=200,window=entry) #位置是圖片中心點，可以用來插入在桌布上面
        
        GUI_Function.__init__(self, parent=self.parent)

        self.initial_user_interface()
        self.chose_textbox()
        self.image_chose_button()
        self.image_open_button()
        self.image_gaus_kernal_button()#會有錯:gaus_kernal only integer scalar arrays can be converted to a scalar index
        self.image_gaus_blur_button()
        self.image_filter2d_button()#會有錯:filter2d() missing 1 required positional argument: 'filter'
        self.image_otsu_thres_button()
        self.image_Log_button()
        self.image_sobel_button()
        
    def initial_user_interface(self):
        self.parent.geometry("1024x720")
        self.parent.resizable(False, False)
        self.parent.title("MEV-DIP_class_Final_project")
    
    #預留column=0和row=0當作預設擴充的地方或是最後要把輸入的按鍵外擴

    def chose_textbox(self):
        self.image_name = ttk.Entry(
              self.parent, width=13, textvariable=self.filename)
        #self.image_name.grid(column=1 ,row=1 , pady=10 ,padx=10 ,ipadx=10 ,ipady=13)
        canvas.create_window(75,26, width=150, height=50,window=self.image_name)
    def image_chose_button(self):
        self.image_chose = ttk.Button(
             self.parent, text="Choosen", command=self.Chose_Image)
        #self.image_chose.grid(column=2, row=1 ,pady=3 ,padx=3 ,ipadx=10 ,ipady=10)#有了下面那行這行就出現不了了
        canvas.create_window(200,26, width=100, height=50,window=self.image_chose)
        

    def image_open_button(self):
        self.image_open = ttk.Button(
            self.parent, text="Show original picture", command=self.open_original_image)
        self.image_open.grid(column=3, row=1,pady=3 ,padx=3 ,ipadx=10 ,ipady=10)

    #gaus_kernal only integer scalar arrays can be converted to a scalar index，所以我沒放上去
    def image_gaus_kernal_button(self) : 
        self.kernal = ttk.Button(self.parent, text="gaus kernal",
                               command=lambda :[self.open_image(),self.gaus_kernal()])
        self.kernal.grid(column=2, row=3,pady=3 ,padx=3 ,ipadx=10 ,ipady=10)
    
    def image_gaus_blur_button(self) :
        self.blur = ttk.Button(self.parent, text="gaus blur",
                               command=lambda :[self.open_image(),self.gaus_blur()])
        self.blur.grid(column=1, row=2,pady=3 ,padx=3 ,ipadx=10 ,ipady=10)

    #filter2d() missing 1 required positional argument: 'filter'
    def image_filter2d_button(self) :
        self.filter2d = ttk.Button(self.parent, text="filter2d",
                               command=lambda :[self.open_image(),self.fil2d()])
        self.filter2d.grid(column=2, row=4,pady=3 ,padx=3 ,ipadx=10 ,ipady=10)

    def image_otsu_thres_button(self) :
        self.otsu = ttk.Button(self.parent, text="otsu",
                               command=lambda :[self.open_image(),self.otsu_thres()])
        self.otsu.grid(column=1, row=3,pady=3 ,padx=3 ,ipadx=10 ,ipady=10)

    def image_Log_button(self) :
        self.Log = ttk.Button(self.parent, text="LoG",
                               command=lambda :[self.open_image(),self.log_function_for_button()])
        self.Log.grid(column=1, row=4,pady=3 ,padx=3 ,ipadx=10 ,ipady=10)

    def image_sobel_button(self) :
        self.sobel = ttk.Button(self.parent, text="Sobel",
                               command=lambda :[self.open_image(),self.sobel_function_for_button()])
        self.sobel.grid(column=1, row=5,pady=3 ,padx=3 ,ipadx=10 ,ipady=10)

if __name__ =='__main__' :
    RootWindow = tk.Tk()
    canvas = tk.Canvas(RootWindow,
        width = 510,      # 指定Canvas元件的寬度 
        height = 380,      # 指定Canvas元件的高度 
        bg = 'blue')      # 指定Canvas元件的背景色 
    im=tk.PhotoImage(file='back.gif')#PhotoImage 只能用gif圖
    canvas.create_image(256,192,image = im)#那裏是圖片的中心點
    canvas.grid()
    

    run = Root(RootWindow)
    RootWindow.mainloop()

