from tkinter import *
from tkinter import messagebox as ms
import os
root=Tk()
root.title("TO DO list")
root.geometry("300x350")
root.resizable(False,False)
filename="data.txt"
def load_text():
    if os.path.exists(filename):
        file1=open(filename,"r")
        for tast in file1.readlines():
            listbox.insert(END,tast.strip())
def save_tast():
    file=open(filename,"w")
    tast=listbox.get(0,END)
    for x in tast:
        file.write(x+"\n")


def add():
    task=entry.get()
    if task=="":
        ms.showwarning("waring ")
    else:
        listbox.insert(END,task)
        entry.delete(0,END)
        save_tast()

def delete():
    try:
        select=listbox.curselection()
        listbox.delete(select)
        save_tast()
    except:
        ms.showwarning("Waring , Select the first task")

Label(root,text="To Do List ",font=("Arial",25)).pack(padx=5)
entry=Entry(root,borderwidth=20,font=("Arial,20"),justify=RIGHT)
entry.pack(padx=5)
btn1=Button(root,text=("Add",15),width=8,height=2,command=add)
btn2=Button(root,text=("Delete",15),width=8,height=2,command=delete)
btn1.pack(padx=5,pady=5)
btn2.pack(padx=5,pady=5)
listbox=Listbox(root,width=50,height=40,font=("Arial",15))
listbox.pack(padx=2,pady=5)

root.mainloop()