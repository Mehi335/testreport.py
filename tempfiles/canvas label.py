from tkinter import *

message = "cheese"
     
canvas = Canvas(width=300, height=300, bg='white', title ='My title')
canvas.pack(expand=YES, fill=BOTH)                   
     
widget = Label(canvas, text=message, fg='white', bg='black')
widget.pack()
canvas.create_window(100, 100, window=widget)       
mainloop()
