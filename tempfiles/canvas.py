import os
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter import messagebox
from tkinter import Tk, Canvas, Frame, BOTH

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
    canvas = Canvas()
    for x in range(7):
        canvas.create_line(15, x * 150 - 50, 1785, x * 150 - 50, dash=(8, 2))
    canvas.create_text(1752, 90, anchor=W, font=("Arial", 12, "bold"), text="+60")
    canvas.create_text(1752, 240, anchor=W, font=("Arial", 12, "bold"), text="+40")
    canvas.create_text(1752, 390, anchor=W, font=("Arial", 12, "bold"), text="+20")
    canvas.create_text(1772, 540, anchor=W, font=("Arial", 12, "bold"), text="0")
    canvas.create_text(1752, 690, anchor=W, font=("Arial", 12, "bold"), text="-20")
    canvas.create_text(1752, 840, anchor=W, font=("Arial", 12, "bold"), text="-40")

    canvas.pack(fill=BOTH, expand=1)
    # ex = Board()

    root.mainloop()

if __name__ == '__main__':
    main()