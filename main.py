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

        GUI_Function.__init__(self, parent=self.parent)

        self.initial_user_interface()
        self.chose_textbox()
        self.image_chose_button()
        self.image_open_button()
        self.image_gus_blur_button()
        self.image_otsu_thres_button()


    def initial_user_interface(self):
        self.parent.geometry("1024x720")
        self.parent.resizable(False, False)
        self.parent.title("DIP")
    
    def chose_textbox(self):
        self.image_name = ttk.Entry(
              self.parent, width=40, textvariable=self.filename)
        self.image_name.grid(column=0 ,row=1 , pady=10 ,padx=10 ,ipadx=3 ,ipady=1)

    def image_chose_button(self):
        self.image_chose = ttk.Button(
             self.parent, text="Choosen", command=self.Chose_Image)
        self.image_chose.grid(column=1, row=1 ,padx=5)

    def image_open_button(self):
        self.image_open = ttk.Button(
            self.parent, text="open", command=self.open_image)
        self.image_open.grid(column=2, row=1)

    def image_gus_blur_button(self) :
        self.blur = ttk.Button(self.parent, text="blur",
                               command=self.gus_blur)
        self.blur.grid(column=2, row=2)
    def image_otsu_thres_button(self) :
        self.otsu = ttk.Button(self.parent, text="otsu",
                               command=self.otsu_thres)
        self.otsu.grid(column=3, row=3)


if __name__ =='__main__' :
    RootWindow = tk.Tk()
    run = Root(RootWindow)
    RootWindow.mainloop()


