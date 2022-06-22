import tkinter as tk
import tkinter.messagebox
from tkinter .constants import SUNKEN

def myclick(num):
    entry.insert(tk.END, num)
def equalto():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0,y)
    except:
        tkinter.messagebox.showinfo("Error","syntax is no good")

def clear():
    entry.delete(0, tk.END)
def clearonce():
    entry.delete(0,tk.END)


window = tk.Tk()
window.title("My Calculator")
frame = tk.Frame(master=window, bg="#99DEAD", padx=30)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=37)
entry.grid(row=0, column=0, columnspan=30, ipady=2, pady=2)

addition = tk.Button(master=frame, text='+', padx=15, pady=5, width=3, command=lambda: myclick("+"))
addition.grid(row=1, column=1, pady=2)
subtraction = tk.Button(master=frame, text='-', padx=15, pady=5, width=3, command=lambda: myclick("-"))
subtraction.grid(row=1, column=2, pady=2)
Multiplication = tk.Button(master=frame, text='x', padx=15, pady=5, width=3, command=lambda: myclick("*"))
Multiplication.grid(row=1, column=3, pady=2)
Division = tk.Button(master=frame, text='÷', padx=15, pady=5, width=3, command=lambda: myclick("/"))
Division.grid(row=1, column=4, pady=2)

Button_1 = tk.Button(master=frame, text='1', padx=15, pady=5, width=3, command=lambda: myclick(1))
Button_1.grid(row=2, column=1, pady=2)
Button_2 = tk.Button(master=frame, text='2', padx=15, pady=5, width=3, command=lambda: myclick(2))
Button_2.grid(row=2, column=2, pady=2)
Button_3 = tk.Button(master=frame, text='3', padx=15, pady=5, width=3, command=lambda: myclick(3))
Button_3.grid(row=2, column=3, pady=2)
Button_4 = tk.Button(master=frame, text='4', padx=15, pady=5, width=3, command=lambda: myclick(4))
Button_4.grid(row=3, column=1, pady=2)
Button_5 = tk.Button(master=frame, text='5', padx=15, pady=5, width=3, command=lambda: myclick(5))
Button_5.grid(row=3, column=2, pady=2)
Button_6 = tk.Button(master=frame, text='6', padx=15, pady=5, width=3, command=lambda: myclick(6))
Button_6.grid(row=3, column=3, pady=2)
Button_7 = tk.Button(master=frame, text='7', padx=15, pady=5, width=3, command=lambda: myclick(7))
Button_7.grid(row=4, column=1, pady=2)
Button_8 = tk.Button(master=frame, text='8', padx=15, pady=5, width=3, command=lambda: myclick(8))
Button_8.grid(row=4, column=2, pady=2)
Button_9 = tk.Button(master=frame, text='9', padx=15, pady=5, width=3, command=lambda: myclick(9))
Button_9.grid(row=4, column=3, pady=2)
Button_equal = tk.Button(master=frame, text='=', padx=15, pady=5, width=3, command=equalto)
Button_equal.grid(row=5, column=4, pady=2)
Button_0 = tk.Button(master=frame, text='0', padx=15, pady=5, width=3, command=lambda: myclick(0))
Button_0.grid(row=5, column=2, pady=2)
Button_Clear1 = tk.Button(master=frame, text='C', padx=15, pady=5, width=3, command=clearonce)
Button_Clear1.grid(row=2, column=4, pady=2)
Button_ClearAll= tk.Button(master=frame, text='CLR', padx=15, pady=5, width=3, command=clear)
Button_ClearAll.grid(row=3, column=4, pady=2)
Button_comma = tk.Button(master=frame, text='.', padx=15, pady=5, width=3, command=lambda: myclick("."))
Button_comma.grid(row=4, column=4, pady=2)

window.mainloop()
