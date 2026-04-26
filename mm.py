from tkinter import *

tk=Tk()
tk.geometry("600x400")
tk.title("калькулятор")

entr=Entry(width=100,font=("arial",25))
entr.pack(anchor="nw")

frame=Frame()
frame.pack(anchor="nw")
tk.mainloop()