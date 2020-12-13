import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
#背景
canvas = tk.Canvas(root, width=480,height=240,bd=0, highlightthickness=0)
imgpath = 'back.gif'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)

canvas.create_image(100, 50, image=photo)
canvas.pack()
entry=tk.Entry(root,insertbackground='blue', highlightthickness =2)
entry.pack()

canvas.create_window(100, 50, width=100, height=20,
                                      window=entry)



root.mainloop()