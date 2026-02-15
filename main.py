from tkinter import *
from tkinter import ttk



root = Tk()
root.title("METANIT.COM")
root.geometry("400x1000")

def finish():
    global vlv
    if combobox.get() == 7:
        vlv+=50
    if sch.get() == 30:
        vlv+=50

value_var = IntVar(value=vlv)
progr=ttk.Progressbar(orient=HORIZONTAL,variable=value_var)
progr.pack(anchor=N)

label=Label(text="сколько будет 2+5?")
label.pack(pady=10)

answervar=IntVar()

answer = [1,2,4,7,6,4,6,5,100,77,68,45]
combobox = ttk.Combobox(values=answer,textvariable=answervar)
combobox.pack(anchor=N,  pady=6)

label2=Label(text="сколько будет 10-7?")
label2.pack(anchor=N,pady=10)

sch=ttk.Scale(orient=HORIZONTAL)
sch.pack(anchor=N)

val = IntVar(value=10)

label3=Label(textvariable=val).pack(anchor=N)

btn=Button(anchor=N,text="завершить",command=finish)
btn.pack()
root.mainloop()