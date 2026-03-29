from tkinter import ttk
import tkinter as tk

root=tk.Tk()
root.geometry("700x450")

columns=["name","people","square"]


tree=ttk.Treeview(columns=columns,show="headings")
tree.pack(anchor="nw",expand=1)

tree.heading("name", text="Название города")
tree.heading("people", text="Население")
tree.heading("square", text="Площадь")

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

def dob():
    global r
    r=[entry.get(),entry2.get(),entry3.get()]
    for person in r:
        tree.insert("", "end",values=person)

btn=ttk.Button(text="добавить",command=dob())
btn.pack(anchor="nw")

root.mainloop()