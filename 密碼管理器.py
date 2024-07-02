# 這是一個帳號密碼管理器，在這個無數平台的世界，我們可能無法記住那麼多的帳號密碼，有了這個程式，我們就可以將自己的帳密
# 保存起來，如此一來就不怕忘記了(需搭配json格式的檔案code.json進行)
import json

print("歡迎使用密碼管理器")                                           # 與使用者互動
while True:                                                       # 此程式可以依值使用值到使用者輸入q，也就是選擇離開時才會停止
    func = input("請問要使用什麼功能呢? (r查詢 a新增 q離開)")            # 選擇功能:查詢新增或離開
    if func == "r":                                               # 查詢功能
        with open("code.json", "r") as file:                      # 打開儲存我們帳密的檔案
            code_dict = json.loads(file.read())                   # 存放到python格式的code_dict以便後續的運算
        name = input("請輸入帳號名稱")                               # 輸入欲查詢帳號
        if name in code_dict:                                     # 如果無此帳號會提示
            print(f"帳號:{code_dict[name]["account"]}, 密碼:{code_dict[name]["password"]}")     # 顯示結果
        else:
            print("無此帳號")
            continue
    elif func == "a":                                             # 新增功能
        with open("code.json", "r") as file:                      # 打開儲存我們帳密的檔案
            code_dict = json.loads(file.read())                   # 存放到python格式的code_dict以便後續的運算
        name = input("請輸入帳號名稱")                               # 輸入欲新增帳號密碼
        acc = input("請輸入帳號")
        code = input("請輸入密碼")
        if name in code_dict:                                     # 已有帳密的帳號名稱會提示
            print("已有此帳號")
            continue

        code_dict[name] = {"account": acc, "password": code}      # 新增到code_dict字典裡

        with open("code.json", "w") as file:
            file.write(json.dumps(code_dict, indent = 4))         # 將字典更新內容回傳到json檔案裡並進行換行及縮排

        print("新增成功")
    elif func == "q":                                             # 輸入q就離開
        print("\n謝謝您的使用~")
        break
    else:                                                         # 輸入r查詢、a新增 或是 q離開以外的會提示
        print("請輸入r查詢、a新增 或是 q離開")
        continue
