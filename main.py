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

        self.width = 200
        self.height = 100
        
        self.central_y = (self.height/2)+30
        self.central_x = (self.width/2)+30
        
        self.offset_x = self.width*9/8
        self.offset_y = self.height*9/8

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
        #self.image_show_label()

    def initial_user_interface(self):
        self.parent.geometry("1600x1000")
        self.parent.resizable(False, False)
        self.parent.title("MEV-DIP_class_Final_project")
    
    #預留column=0和row=0當作預設擴充的地方或是最後要把輸入的按鍵外擴
    '''
    def image_show_label(self):#這些是柏鑫測試的東西
        #image_path = self.show_image_on_window()
        #self.image =super().OpenImage(image_file_name = self.image_path , methood="cv")
        my_image=tk.PhotoImage(file='ccit.gif')
        self.image_label = ttk.Label(self.parent,image=my_image)
        canvas.create_window(self.central_x+3*self.offset_x,self.central_y+5*self.offset_y,
                             width=444, height=444,window=self.image_label)
    
        my_image = Image.open(jpg)
        resized = my_image.resize((320, 240), Image.ANTIALIAS)
        my_image = ImageTk.PhotoImage(resized)
        my_image_label = tk.Label(image=my_image)
        my_image_label.place(x=5, y=140)
    '''#這些是柏鑫測試的東西
    def chose_textbox(self):
        self.image_name = ttk.Entry(
              self.parent, width=13, textvariable=self.filename)
        #self.image_name.grid(column=1 ,row=1 , pady=10 ,padx=10 ,ipadx=10 ,ipady=13)
        canvas.create_window(self.central_x+150,self.central_y, width=self.width+300, height=self.height,window=self.image_name)
    
    def image_chose_button(self):
        self.image_chose = ttk.Button(
             self.parent, text="Choosen", command=self.Chose_Image)
        #self.image_chose.grid(column=2, row=1 ,pady=3 ,padx=3 ,ipadx=10 ,ipady=10)#有了下面那行這行就出現不了了
        canvas.create_window(self.central_x+self.offset_x+300,self.central_y, width=self.width, height=self.height,window=self.image_chose)
        

    def image_open_button(self):
        self.image_open = ttk.Button(
            self.parent, text="Show original picture", command=self.open_original_image)
        #self.image_open.grid(column=3, row=1,pady=3 ,padx=3 ,ipadx=10 ,ipady=10)
        canvas.create_window(self.central_x+2*self.offset_x+300,self.central_y,
                             width=self.width, height=self.height,window=self.image_open)
    
    #gaus_kernal only integer scalar arrays can be converted to a scalar index，所以我沒放上去
    def image_gaus_kernal_button(self) : 
        self.kernal = ttk.Button(self.parent, text="gaus kernal",
                               command=lambda :[self.open_image(),self.gaus_kernal()])
        #self.kernal.grid(column=2, row=3,pady=3 ,padx=3 ,ipadx=10 ,ipady=10)
        canvas.create_window(self.central_x+self.offset_x,self.central_y+self.offset_y,
                             width=self.width, height=self.height,window=self.kernal)

    def image_gaus_blur_button(self) :
        self.blur = ttk.Button(self.parent, text="gaus blur",
                               command=lambda :[self.open_image(),self.gaus_blur()])
       # self.blur.grid(column=1, row=2,pady=3 ,padx=3 ,ipadx=10 ,ipady=10)
        canvas.create_window(self.central_x,self.central_y+self.offset_y,
                             width=self.width, height=self.height,window=self.blur)

    #filter2d() missing 1 required positional argument: 'filter'
    def image_filter2d_button(self) :
        filt = super().gaussian_kernal(size = 3)
        self.filter2d = ttk.Button(self.parent, text="filter2d",
                               command=lambda :[self.open_image(),self.fil2d()])
        #self.filter2d.grid(column=2, row=4,pady=3 ,padx=3 ,ipadx=10 ,ipady=10)
        canvas.create_window(self.central_x+self.offset_x,self.central_y+2*self.offset_y,
                             width=self.width, height=self.height,window=self.filter2d)

    def image_otsu_thres_button(self) :
        self.otsu = ttk.Button(self.parent, text="otsu",
                               command=lambda :[self.open_image(),self.otsu_thres()])
        #self.otsu.grid(column=1, row=3,pady=3 ,padx=3 ,ipadx=10 ,ipady=10)
        canvas.create_window(self.central_x,self.central_y+2*self.offset_y,
                             width=self.width, height=self.height,window=self.otsu)

    def image_Log_button(self) :
        self.Log = ttk.Button(self.parent, text="LoG",
                               command=lambda :[self.open_image(),self.log_function_for_button()])
        #self.Log.grid(column=1, row=4,pady=3 ,padx=3 ,ipadx=10 ,ipady=10)
        canvas.create_window(self.central_x,self.central_y+3*self.offset_y,
                             width=self.width, height=self.height,window=self.Log)


    def image_sobel_button(self) :
        self.sobel = ttk.Button(self.parent, text="Sobel",
                               command=lambda :[self.open_image(),self.sobel_function_for_button()])
        #self.sobel.grid(column=1, row=5,pady=3 ,padx=3 ,ipadx=10 ,ipady=10)
        canvas.create_window(self.central_x,self.central_y+4*self.offset_y,
                             width=self.width, height=self.height,window=self.sobel)

if __name__ =='__main__' :
    RootWindow = tk.Tk()
    canvas = tk.Canvas(RootWindow,
        width = 1600,      # 指定Canvas元件的寬度 
        height = 1000,      # 指定Canvas元件的高度 
        bg = 'blue')      # 指定Canvas元件的背景色 
    im=tk.PhotoImage(file='background.gif')#PhotoImage 只能用gif圖
    canvas.create_image(800,500,image = im)#那裏是圖片的中心點
    im1=tk.PhotoImage(file='ccit.gif')
    canvas.create_image(1370,224,image = im1)#放上校徽整個感覺就不一樣了
    canvas.grid()
    
    run = Root(RootWindow)
    RootWindow.mainloop()

