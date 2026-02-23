from tkinter import *
from tkinter import messagebox as ms
bass=Tk()
bass.title("GUI Unit Converter")
bass.geometry("400x400")
bass.resizable(False,False)
Label(bass,text="Unit Converter",font=("Arial",20)).pack(pady=5)
dis=Entry(bass,font=("Arial",15),borderwidth=5,justify=CENTER)
dis.pack(padx=5)
result=Label(bass,text="Result",font=("Arial",20))
result.pack(padx=5,pady=5)
opt=[
    "Km to Meter",
    "Meter to Km",
    "Celsius to Fahrenheit",
    "Fahrenheit to Celsius",
    "Kg to Gram",
    "Gram to Kg"
]
choice = StringVar()
choice.set(opt[0])
OptionMenu(bass,choice,*opt).pack(padx=10)
def convert():
    try:
        val=float(dis.get())
        sel=choice.get()
        if sel=="Km to Meter":
            res=val*1000
        elif sel=="Meter to Km":
            res=val/1000
        elif sel=="Celsius to Fahrenheit":
            res = (val * 9/5) + 32
        elif sel=="Fahrenheit to Celsius":
            res=(val - 32) * 5/9
        elif sel=="Kg to Gram":
            res=val*1000
        elif sel=="Gram to Kg":
            res=val/1000
        result.config(text=(f"Result={res}"),font=("Arial",20))
    except ValueError:
        ms.showerror("error","Pls Enter The valid Number ")
def delet():
    dis.delete(0,END)
def delet_result():
    delet()
    result.config(text="Result")

Button(bass,text=("Convert"),font=("Arial",10),borderwidth=5,command=convert).pack(padx=5,pady=5)
Button(bass,text='Clear',font=("Arial",10),borderwidth=5,command=delet_result).pack(padx=5,pady=5)
bass.mainloop()