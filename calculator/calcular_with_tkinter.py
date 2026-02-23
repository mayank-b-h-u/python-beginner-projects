from tkinter import *
root=Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False,False)
#entery point
enter=Entry(root,font=("Arial ",),borderwidth=5,justify=RIGHT)
enter.pack(padx=5,pady=5)
#funtion to add the number
def add_num(num):
    enter.insert(END,num)
#funtion to clear
def delet():
    enter.delete(0,END)
def calcul():
    try:
        result=eval(enter.get())
        enter.delete(0,END)
        enter.insert(END,result)
    except:
        enter.delete(0,END)
        enter.insert(END,'Error')
frame=Frame(root)
frame.pack()
btn=[
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
    ]
col=0
row=0
for bt in btn:
    if bt =="=":
        b=Button(frame,text=bt,width=5,height=2,font=("Arial",14),command=calcul)
    else:
        b=Button(frame,text=bt,width=5,height=2,font=("Arial",14),command= lambda x=bt: add_num(x))
    b.grid(column=col,row=row,padx=5,pady=5)
    col+=1
    if col>3:
        col =0
        row+=1
frame1=Frame(frame)
Button(root,text='Clear',font=("Arial",20),width=20,height=5,command=delet).pack(padx=5,pady=5)
root.mainloop()