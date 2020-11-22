from tkinter import Tk, Canvas, Frame, BOTH, W, Widget,ttk
from tkinter import *

class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.master.title('Lab 9 A & B')
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)

        canvas.create_rectangle(200, 10, 270, 200,
          outline="black", fill="white", width=2)
        
        canvas.create_line(235, 15, 235 , 195, width = 2)
    
        canvas.create_text(180 ,199, anchor = W, font ='Calibri', text='0')
        canvas.create_text(175 ,159, anchor = W, font ='Calibri', text='20')
        canvas.create_text(175 ,119, anchor = W, font ='Calibri', text='40')
        canvas.create_text(175 ,79, anchor = W, font ='Calibri', text='60')
        canvas.create_text(175 ,39, anchor = W, font ='Calibri', text='80')
        canvas.create_text(165 ,9, anchor = W, font ='Calibri', text='100', fill = "red")
        
        coordY = 24
        for x in range(0, 5):
            canvas.create_line(200,coordY,210,coordY, width = 2)
            coordY +=38
        
        canvas.create_line(230, 50, 240, 50, fill="red",width = 5)
        canvas.pack(fill=BOTH, expand=1)

root = Tk()
ex = Example()
inputtxt = Text(frame, height = 1,  width = 10, bg = "light yellow")
inputtxt.pack()
root.geometry('600x250+300+300')
root.mainloop()
    


