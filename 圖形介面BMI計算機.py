from tkinter import *


def calculation():
    num1 = float(height.get())
    num2 = float(weight.get())
    bmi = round(num2/((num1/100)**2), 2)
    my_bmi["text"] = f"您的BMI:{bmi}"


window = Tk()
window.title("BMI計算機")
window.geometry("300x300")
window.config(padx=50,pady=50)

label_height = Label(text="身高")
label_height.grid(row=0, column=0)
label_weight = Label(text="體重")
label_weight.grid(row=1, column=0)
cm = Label(text="公分")
cm.grid(row=0, column=2)
kg = Label(text="公斤")
kg.grid(row=1, column=2)
my_bmi = Label(text="您的BMI:0")
my_bmi.grid(row=2, column=1)

height = Entry()
height.grid(row=0, column=1)
weight = Entry()
weight.grid(row=1, column=1)

butt = Button(text="計算", font=("標楷體", 10), command=calculation)
butt.grid(row=3, column=1)

window.mainloop()