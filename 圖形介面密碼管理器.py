from tkinter import *
from PIL import ImageTk as Ima
import json


def account_management():
    with open("code.json", "r") as file:
        accounts = json.loads(file.read())

    accounts[enter_name.get()] = {enter_acc.get(): enter_code.get()}

    with open("code.json", "w") as file:
        file.write(json.dumps(accounts))


window = Tk()
window.config(padx=50, pady=50)

img = Ima.PhotoImage(file="lock.png")
can = Canvas(width=224, height=225)
can.create_image(112, 112, image=img)
can.grid(row=0, column=0, columnspan=2)

name = Label(text="帳號名稱")
name.grid(row=1, column=0)
acc = Label(text="帳號")
acc.grid(row=2, column=0)
code = Label(text="密碼")
code.grid(row=3, column=0)

enter_name = Entry(width=25)
enter_name.grid(row=1, column=1)
enter_acc = Entry(width=25)
enter_acc.grid(pady=5, row=2, column=1)
enter_code = Entry(width=25)
enter_code.grid(row=3, column=1)

butt = Button(text="新增", width=35, bg="#0066CC", fg="white", command=account_management)
butt.grid(pady=10, row=4, column=0, columnspan=2)

window.mainloop()
