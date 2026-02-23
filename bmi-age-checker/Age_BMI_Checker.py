from tkinter import *
from datetime import date

bass = Tk()
bass.geometry("400x400")
bass.resizable(False, False)
bass.title("Age BMI Checker")

Label(bass, text="Age Checker", font=("Arial", 20)).pack(pady=10)


Label(bass, text="Enter DOB (DD-MM-YYYY)").pack()
dob_entry = Entry(bass, font=("Arial", 12))
dob_entry.pack(pady=5)


dis_category = Entry(bass, font=("Arial", 14), borderwidth=3)
dis_category.pack(pady=5)

dis_age = Entry(bass, font=("Arial", 14), borderwidth=3)
dis_age.pack(pady=5)

def calculate_age():
    dis_category.delete(0, END)
    dis_age.delete(0, END)

    try:
        day, month, year = map(int, dob_entry.get().split("-"))
        today = date.today()

        age = today.year - year
        if (today.month, today.day) < (month, day):
            age -= 1

        dis_age.insert(END, age)

        if age < 18:
            dis_category.insert(END, "Child")
        elif age < 60:
            dis_category.insert(END, "Adult")
        else:
            dis_category.insert(END, "Senior")

    except:
        dis_category.insert(END, "Invalid DOB")

Button(bass, text="Check Age", command=calculate_age).pack(pady=10)

bass.mainloop()