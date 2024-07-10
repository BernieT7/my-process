from tkinter import *
from tkinter import messagebox
from PIL import ImageTk as Ima
import json


def get_dic():
    try:
        with open("code.json", "r") as file:
            dic = file.read()
    except FileNotFoundError:
        with open("code.json", "w") as file:
            return {}
    else:
        if dic == "":
            return {}
        else:
            return json.loads(dic)


def account_management():
    if enter_name.get() == "" or enter_acc.get() == "" or enter_code.get() == "":
        messagebox.showerror(title="新增失敗", message="輸入框不可為空")
    else:
        accounts = get_dic()

        if enter_name.get() in accounts:
            messagebox.showerror(title="新增失敗", message="已有此帳號名稱")
        else:
            accounts[enter_name.get()] = {"account": enter_acc.get(), "password": enter_code.get()}
            with open("code.json", "w") as file:
                file.write(json.dumps(accounts))

            messagebox.showinfo(title="新增成功", message="新增成功")

        enter_name.delete(0, "end")
        enter_acc.delete(0, "end")
        enter_code.delete(0, "end")


def search():
    accounts = get_dic()

    a = enter_name.get()
    if a in accounts.keys():
        account = accounts[a]["account"]
        password = accounts[a]["password"]
        messagebox.showinfo(title=a, message=f"帳號:{account}\n密碼:{password}")
    else:
        messagebox.showwarning(title="搜尋失敗", message="無此帳號名稱")


window = Tk()
window.config(padx=50, pady=50)

img = Ima.PhotoImage(file="密碼管理器/lock.png")
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

find = Button(text="查詢", width=35, bg="#8E8E8E", fg="white", command=search)
find.grid(pady=10, row=4, column=0, columnspan=2)

add = Button(text="新增", width=35, bg="#0066CC", fg="white", command=account_management)
add.grid(row=5, column=0, columnspan=2)

window.mainloop()
