from tkinter import ttk
import tkinter as tk

root=tk.Tk()
root.geometry("700x450")

columns=["name","people","square"]

tree=ttk.Treeview(columns=columns,show="headings",selectmode="extended")
tree.pack(anchor="nw",expand=1)

a=tree.heading("name", text="Название города")
b=tree.heading("people", text="Население")
c=tree.heading("square", text="Площадь")

frame=ttk.Frame()
frame.pack(anchor="nw",pady=10)
label=ttk.Label(frame,text="Название города")
label.pack(side="left")
entry=ttk.Entry(frame)
entry.pack(side="left")

frame2=ttk.Frame()
frame2.pack(anchor="nw")
label2=ttk.Label(frame2,text="Население")
label2.pack(side="left")
entry2=ttk.Entry(frame2)
entry2.pack(side="left",pady=10)

frame3=ttk.Frame()
frame3.pack(anchor="nw")
label3=ttk.Label(frame3,text="Площадь")
label3.pack(side="left")
entry3=ttk.Entry(frame3)
entry3.pack(side="left",pady=10)

def country():
    a = tree.heading("name", text="Название страны")
    label.config(text="Название страны")
    tree.delete(*tree.get_children())

def town():
    a = tree.heading("name", text="Название города")
    label.config(text="Название города")
    tree.delete(*tree.get_children())

radio=ttk.Radiobutton(text="town",command=town)
radio.pack(anchor="ne")
radio=ttk.Radiobutton(text="country",command=country)
radio.pack(anchor="ne")

def dob():
    global r
    r=[entry.get(),entry2.get(),entry3.get()]

    tree.insert("", "end",values=r)

btn=ttk.Button(text="добавить",command=dob)
btn.pack(anchor="nw")

def sort():
    l = [tree.item("IOO1"vyhbgg,"people")]
    print(l)

btnn=ttk.Button(text="сортировать",command=sort)
btnn.pack(anchor="center")
root.mainloop()