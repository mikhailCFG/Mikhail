from tkinter import *
import tkinter as ttk

root=ttk.Tk()
root.geometry("400x1000")
root.title("опросник")

totalanswer=Label(anchor=CENTER,text="отвечайте ниже:")
totalanswer.pack()

correctanswer=0

def finish():
    global correctanswer
    answerAge=entry.get().strip()
    answername=entry2.get().strip()

    if manVar.get() == "m":
        gender="мужской"
    else:
        gender="женский"

    if str(monthVar.get())=="12":
        correctanswer +=1
    resultmessage=f"ваши результаты:\n Возраст:{answerAge}\nИмя:{answername}\nпол:{gender},\nправильных ответов:{correctanswer}"
    totalanswer.config(text=resultmessage)

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

manVar=StringVar(value="none")
man=Radiobutton(anchor=N,text="мужской",value="m",variable=manVar)
man.pack()

woman=Radiobutton(anchor=N,text="женский",value="wm",variable=manVar)
woman.pack()

label4=Label(text="сколько месяцев в году?")
label4.pack(pady=40)

monthVar=IntVar(value=0)

btn=Radiobutton(text="4",value="4", variable=monthVar)
btn.pack()

btn2=Radiobutton(text="9",value="9", variable=monthVar)
btn2.pack()

btn3=Radiobutton(text="12",value="12", variable=monthVar)
btn3.pack()

label5=Label(text="какие числа больше 5:")
label5.pack(pady=40)


btnfinish=Button(text="завершить",command=finish)
btnfinish.pack()


root.mainloop()