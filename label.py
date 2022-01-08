from tkinter import *

ws = Tk()
ws.title("Border")
ws.geometry("300x400")

Label(ws, text="Hello there!", font=("arial italic", 18) ).place(100, 100).pack()

ws.mainloop()
