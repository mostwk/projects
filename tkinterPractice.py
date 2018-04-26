import psutil
from tkinter import *
import time


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = Button(self)
        self.hi_there["text"] = "add 5"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        self.label = Label(self, text="0", bg='blue')
        self.label.pack()
        self.quit = Button(self, text="QUIT", fg="red", command=root.destroy)
        self.quit.pack(side="bottom")
        self.ram = Label(self, bg='gray')
        self.ram.pack()

    def say_hi(self):
        self.label['text'] = str(int(self.label['text']) + int(5))
        battery = psutil.sensors_battery()
        self.ram['text'] = battery.percent


root = Tk()
app = Application(master=root)
app.mainloop()

