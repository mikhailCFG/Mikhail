import tkinter
from tabnanny import check
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("700x400")

notebook=ttk.Notebook()
notebook.pack(fill=BOTH)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook,)
frame3=ttk.Frame(notebook)
frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
frame3.pack(fill=BOTH,expand=True)

notebook.add(frame1, text="код",  compound=RIGHT)
notebook.add(frame2, text="настройки", compound=LEFT)
notebook.add(frame3,text="файлы")

text=Text(frame1,background="black",fg="white",borderwidth=5,height=50)
text.pack()

label=Label(frame2,text="тема",font=("arial",12))
label.pack(anchor=NW,padx=10)

radio=ttk.Checkbutton(frame2,text="черная")
radio.pack(anchor=NW,padx=5)
radio2=ttk.Checkbutton(frame2,text="белая")
radio2.pack(anchor=NW,padx=5)

label2=Label(frame2,text="яркость")
label2.pack(anchor=NW)
prog=ttk.Progressbar(frame2,value=50)
prog.pack(anchor=NW,)
label3=Label(frame2,text=f"50%")
label3.pack(anchor=NW,)



root.mainloop()