from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo,showwarning
root=Tk()
root.geometry("700x450")
root.title("калькулятор")

znak=["+","-","*","/"]


label=ttk.Label(text="первое число")
label.pack(anchor="nw")

entr=ttk.Entry()
entr.pack(anchor="nw")

label2=ttk.Label(root,text="второе число")
label2.pack(anchor="nw")

entr2=ttk.Entry(root)
entr2.pack(anchor="nw")

firstnumber=entr.get()
secondnumber=entr2.get()

def counter():
    window=Tk()

    global a

    combo=ttk.Combobox(window,values=znak)
    combo.pack(anchor="nw")
    a=combo.get()

btn=ttk.Button(text="знак",command=counter)
btn.pack(anchor="nw",pady=10)

def schet():
    global result
    if a == "+":
        result=firstnumber+secondnumber
        showinfo("результат",message=result)

btn4=ttk.Button(text="=",command=schet)
btn4.pack(anchor="nw",pady=10)

root.mainloop()