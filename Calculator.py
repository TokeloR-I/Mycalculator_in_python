import tkinter as tk
import tkinter.messagebox
from tkinter .constants import SUNKEN

def myclick(num):
    entry,insert(tk.END, num)
def equalto():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error","syntax is no good")
def clear():
    entry.delete(0, tk.END)

window = tk.Tk()
window.title("the amazing calculator app")

frame = tk.frame(master=window, bg="skyblue", padx=10)
frame.pack()

#entry = tk.Frame(master=frame, relief=SUNKEN, borderwidth = 3, width = 30)
#entry.grid(row=0,column=0,columnspan=3,ipday = 2,pady=2)

window.mainloop()
