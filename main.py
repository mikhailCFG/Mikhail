from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter as tk

root=tk.Tk()
root.geometry("500x500")

editor=ScrolledText(wrap="word")
editor.pack(anchor=NW)

frame=Frame()
frame.pack(anchor=NW)

def delete():
    editor.delete(1.0,END)

button=Button(frame,text="очистить",command=delete)
button.pack(side=LEFT)

def save():
    a=editor.get(1.0,END)
    file=open("save.txt","w",encoding="UTF-8")
    file.write(a)

btn=Button(frame,text="сохранить",command=save)
btn.pack(side=LEFT)

def zzzz():
    w=open("save.txt","r")
    editor.delete(1.0,END)
    editor.insert(1.0,w.read())

btn2=Button(frame,text="загрузить",command=zzzz)
btn2.pack(side=LEFT)

def schet():
    s=editor.get(1.0,END)
    answer=len(s)
    answer-=1
    root.title(answer)

btn3=Button(frame,text="подсчитать символы",command=schet)
btn3.pack(side=LEFT)

frame2=Frame()
frame2.pack(anchor=NW)

def yellow():
    d=editor.selection_get()
    editor.tag_add("yellow_tag","sel.first","sel.last")
    editor.tag_configure("yellow_tag",background="yellow")

btn4=Button(frame2,text="желтый",background="yellow",command=yellow)
btn4.pack(side=LEFT)

root.mainloop()