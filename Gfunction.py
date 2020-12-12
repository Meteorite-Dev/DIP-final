'''
這裡是寫 GUI 的 動作

只要寫動作的部分，底下的影響處理寫在 IM_classical.py

然後請先理解所有程式。

'''
import tkinter as tk 
from tkinter import filedialog ,ttk

from ImageProcess.process import ImageProcess

class GUI_Function (tk.Frame ,ImageProcess):

    def __init__(self ,parent):
        tk.Frame.__init__(self, parent)
        ImageProcess.__init__(self)

        self.parent = parent

        filename = "Choosen a Image (.jpg / .png)"
        self.filename = tk.StringVar(self.parent, value=filename)
    
    def Chose_Image(self):
        file = filedialog.askopenfilename(initialdir="./",
                                          title="chose a image.", filetypes=(("png files", "*.png"), ("jpeg files", "*.jpg")))
        self.filename = tk.StringVar(self.parent, value=file)
        self.image_name.delete(0 ,"end")
        self.image_name.insert(0, file)
        
        # self.image_name = ttk.Entry(
        #     self.parent, width=len(file)-5, textvariable=self.filename)
        # self.image_name.grid(column=0, row=1, pady=10,
        #                      padx=10, ipadx=3, ipady=1)

    def open_image(self):
        self.image_path = self.image_name.get()
        print(self.image_path)
        # self.image_file_name = image_path
        self.image =super().OpenImage(image_file_name = self.image_path , methood="cv")
        #super().show(image= self.image ,methood="cv")

    def gus_blur(self):
        image_path = self.image_path
        print(image_path)
        image = super().Gaussian_filter(self.image)
        image = super().CV2PIL(image)
        super().show(image = image)
    def otsu_thres(self):
        image_path = self.image_path
        print(image_path)
        image = super().otsu_threshold(self.image)
        image = super().CV2PIL(image)
        super().show(image = image)
            
if __name__ =="__main__" :
    G = GUI_Function(tk.Tk())
    G.OpenImage("okayu.png")
                        


