import os
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter import messagebox
from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        for x in range(7):
            canvas.create_line(15, x*150-100, 1785, x*150-100, dash=(4,2))
        canvas.create_text(1750, 40, anchor=W, font=("Arial", 12), text="+60")
        canvas.create_text(1750, 190, anchor=W, font=("Arial", 12), text="+40")
        canvas.create_text(1750, 340, anchor=W, font=("Arial", 12), text="+20")
        canvas.create_text(1750, 490, anchor=W, font=("Arial", 12), text="0")
        canvas.create_text(1750, 640, anchor=W, font=("Arial", 12), text="-20")
        canvas.create_text(1750, 790, anchor=W, font=("Arial", 12), text="-40")

        canvas.pack(fill=BOTH, expand=1)


def main():
    il_file_name = "C:/google drive/python/temptest_log_reader/ildata.txt"
    temp_file_name = "C:/google drive/python/temptest_log_reader/tempdata.TXT"
    result_file_name = "C:/google drive/python/temptest_log_reader/results.txt"
    il_limit_value = 0.08

    """Main window"""
    root = Tk()
    root.title('Temperature cycling test log file parser')
    root.resizable(False, False)
    root.geometry('1800x900')
    ex = Example()

    root.mainloop()

if __name__ == '__main__':
    main()