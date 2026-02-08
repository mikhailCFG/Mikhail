from tkinter import *
import tkinter as ttk

root=ttk.Tk()
root.geometry("400x1000")
root.title("опросник")

totalanswer=Label

correctanswer=0
def finish():
    global finish
    totalanswer(text=f"имя: {entry2} возраст: {entry}")
    totalanswer.pack()
label=Label(anchor=N,text="введите свой возраст")
label.pack(pady=20)

entry=Entry()
entry.pack()

label2=Label(anchor=N,text="введите свое имя")
label2.pack(pady=20)

entry2=Entry()
entry2.pack()

label3=Label(anchor=N,text="ваш пол")
label3.pack(pady=20)

man=Radiobutton(anchor=N,text="мужской",value="мужской",)
man.pack()

woman=Radiobutton(anchor=N,text="женский",value="женский")
woman.pack()

label4=Label(text="сколько месяцев в году?")
label4.pack(pady=40)

btn=Radiobutton(text="4",value="4")
btn.pack()

btn2=Radiobutton(text="9",value="9")
btn2.pack()

btn=Radiobutton(text="12",value="12")
btn.pack()

btnfinish=Button(text="завершить",command=finish)
btnfinish.pack()
root.mainloop()