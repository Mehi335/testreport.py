# Imports all (*) classes,
# atributes, and methods of tkinter into the
# current workspace

import tkinter as tk
#import tkinter.messagebox as messagebox

def il_get_value():
    # ***********************************
    # Creates an instance of the class tkinter.Tk.
    # This creates what is called the "root" window. By conventon,
    # the root window in Tkinter is usually called "root",
    # but you are free to call it by any other name.

    il_get_window = tk.Tk()
    il_get_window.title('TestGraph')

    mystring = tk.StringVar()
    number_float = 0

    def getvalue():
        try:
            number_float = float(mystring.get())
            il_get_window.destroy()
        except:
            messagebox.showerror("Not a number!", "Decimal number format should be 0.00")

    tk.Label(il_get_window, text="IL limit for 1 connector (0.08 by default) : ").grid(row=0, sticky=tk.W)  # label
    tk.Entry(il_get_window, textvariable=mystring).grid(row=0, column=1, sticky=tk.E)  # entry textbox
    WSignUp = tk.Button(il_get_window, text="Apply", command=getvalue).grid(row=0, column=4, sticky=tk.W)  # button

    il_get_window.mainloop()
    return float(mystring.get())


print(il_get_value())
