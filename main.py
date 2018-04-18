import psutil
from tkinter import *

base_window = Tk()
topFrame = Frame(base_window)
topFrame.pack()
bottomFrame = Frame(base_window)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="grey")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="red")
button4 = Button(bottomFrame, text="Button 4", fg="black")
button1.pack(side=TOP)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()
base_window.mainloop()

