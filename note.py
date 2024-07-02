# print("") 印文字
# input("提示語句") 使用者輸入(資料型態為字串喔)
# print(input("")) 會印出使用者輸入內容
# print("" + input("")) 可印出文字加使用者輸入內容
# x=""變數替換指定內容
# x=input("")變數替換使用者輸入內容
# 變數命名規則：
#     1.只能是字母、數字、_的組合
#     2.開頭不能是數字
#     3.不能是關鍵字
# 資料型態：  
#     字串string："文字"
#     整數int：(直接寫數字就好不用引號)
#     小數float：(直接寫小數數字就好不用引號)
#     布林值boolean：True/False
# pinrt(""[n])可以取得字串中的第(n+1)個字
# type()檢驗資料型態
# 轉換資料型態：
#     1.int()換整數
#     2.float()換浮點數
#     3.str()換字串
# 字串中引號中還有引號，解決方法：
#     1.print('....",,"....')
#     2.print("....\",,,\"....")
# \n 換行
# 資料型態不同轉字串相加：
#     1.print("..." + str(age) + ",,," + str(is_male))
#     2.print(f"...{age},,,{is_male}")
# 運算符號：+,-,*,/,//(把小數點去點),**(次方),%(取除法餘數)
# round(x,n)對x四捨無入到小數點後n位數
# 自己對自己運算：
#     1.(num = num + n)=(num += 10)
#     2.(num = num * n)=(num *= 10)
#     3.(num = num / n)=(num /= 10)
# if 語句：
#     if 條件:
#         條件成立要做的事
#     else:
#         條件不成立要做的事
# 判斷左右是否相等時要用：
#     a == b而不是a = b，一個等於意思是令右邊等於左邊
# 不相等的判斷符號：!=
# elif 語句(有多個條件時使用)(任條件成立後，其以下的條件都會被跳過):
#     if 條件1:
#         條件成立要做的事
#     elif 條件2:
#         條件成立要做的事
#     elif 條件3:
#         條件成立要做的事
#     else:
#         條件不成立要做的事
# 巢狀if:
# if  條件:
#     if 條件中的條件:
#         條件成立要做的事
#     else:
#         條件不成立要做的事
# else:
#     條件不成立要做的事
# 注意：if的條件不能寫雙重判斷(例如:0<x<1)，只能寫一個:
# if x<0:
# elif x<1
# 這樣寫就是0<x<1的意思，因為程式會由上到下運行
# 邏輯運算:
#     and且(兩邊都成立才True)。a and b
#     or或(任一邊成立則True)。a or b
#     not反敘述。not a
# 將使用者輸入字串中英文字母全部改大寫OR改小寫
#     input().upper()大寫
#     input().lower()小寫
# 創建函數:
#     def 函數名稱(參數):
#         內容
#         參數
#         .
#         .
#         .
#     函數名稱()     呼叫函數
# 關於函數與參數:
#     1.函數數可被傳入參數也可傳出參數
#     2.參數多容易輸入順序錯誤，此時可以用指定的方式避免
#         def function_1(a, b, c)
#             content
#         function_1(b = 2, c = 3, a = 1)
#     3.為什麼需要函數？當某個龐大計算或邏輯需重複使用時，函式可以濃縮程式
#     4.函數回傳:return
#         def function_1(a, b, c)
#             content
#             return cool
#        test = def function_1(a, b, c)
#        其實等於 test = cool
#        注意函數遇到return會使函數中return以下的程式碼都不被執行
#     5.避免參數型態錯誤:
#         if type(a) != int or type(b) != int or type(c) != int:
#             return "請輸入整數"  
# module 模組：(就是把許多函數變成一個工具箱存入另一個檔案，要用的時候呼叫他就好，這樣主檔案的畫面會比較乾淨)
#     呼叫方式：import 模組名--->模組名.模組內函式(參數)
# random 模組
#     1.random.randint(a,b) 隨機生成[a,b]任意整數
#     2.random.random()隨機生成[0,1)任意浮點數
#         補：random.random()*n 即可生成[0,n)任意浮點數
#     3.random.shuffle(list名稱) 隨機打亂list(注意不能打亂str，只能打亂list)
#     4.random.sample(list名稱, n) 從list中隨機挑出n筆資料
# 列表 list(為一種資料型態，可以存多筆資料):
#     1.表示方法:list名稱 = [a, b, c, ...]
#     2.list名稱[n] list中第n+1筆資料
#     3.list名稱[-n] list中倒數第n筆資料
#     4.列表中的資料型態可以不一致:(EX:[1, 2, true, "HI"])
#     5.list名稱.append(欲加入資料) 加入新資料
#     6.list名稱.count(list中某資料) 可得知list中某資料共出現幾次
#     7.list名稱.insert(a, b) 在第a筆資料插入b這筆新資料
#     8.list名稱.remove(b) 刪除list中第一筆出現的b
# 字串分割:字串名稱.split("欲分割的符號")
# 取得字串長度:len(字串名稱)
# 取得list中任意一筆資料:random.randint(0, len(字串名稱)-1)
# nested list巢狀列表:(列表中的列表)
#     EX:[[1,2,3],2,4,7,[2,3,7],6]
#     1.list名稱[n][m] 取得第n筆資料中的第m筆資料
#     2.矩陣:巢狀列表每一筆資料的大小都一樣
#        EX:[
#            [1,2,3],
#            [4,5,6],
#            [7,8,9]
#           ]
#     3.矩陣念法:n*m指的是n row行, m colunm列(程設裡面為 直列橫行)
#     4.list名稱[n][m] 取得第n row 第m colunm 資料
#     5.取得n為列表的值:list名稱[][][]...共n個中括號
# """內容""" 這樣換行時直接按ENTER 就會自動幫你換行
# while迴圈:重複執行直到條件判斷為false
#     1.寫法:while 條件判斷:
#               要重複執行的程式
# for迴圈:可以依序一一取字串中的每一個字or list的每一筆資料，並重複執行某程式碼
#     1.寫法:for item in 字串或list:(item為一一取出的資料暫存位置，不一定叫item也沒關係)
#               要重複執行的程式
#     2.常與range()搭配
#       寫法:for i in range(a, b):(重複執行b-a次)
#               要重複執行的程式
# range(n, m)函數:
#     1.[n, n+1, ..., m-1] 注意!不包函m
#     2.range(n, m, t)第三個參數t代表的是每一個數之間的間隔大小
# list(字串) 把字串逐字變列表
# 字典 dictionary:輸入"key"配對到一個"value"
#     (EX:輸入:"蘋果"，配對到"apple")
#     1.創建字典寫法:
#          字典名稱 = {
#               key1: value1, 
#               key2, value2
#               ...
#                }
#     2.取字典值:字典名稱[key名稱]
#     3.字典不對型態設限制
#     4.更改/新增字典的值:字典名稱[key名稱] = 值
#     5.與for loop的搭配使用:
#         for item in 字典名稱:
#             print(item)                取得所有key
#             print(字典名稱[item])           取得所有value
#     6.如果key所對應的value為list型態，取得該list第n筆資料方式為:
#         字典名稱[key][n-1]
#     7.如果key所對應的value為另一字典，取得另一字典資料方式為:
#         字典名稱[原字典key][另一字典的key]
#     8.list中的資料型態可以為字典:
#         (EX:[1, 2, {key1: value1, key2: value2,...}, 5, 6])
#         取得方式:list名稱[2][key]
#     9.回傳所有keys:字典名稱.keys() 注意回傳結果不是list
#     10.回傳所有values:字典名稱.values() 注意回傳結果不是list
# 區域變數:函式內部的變數，只有函式內有效，函式外無效
#     1.函式與函式之間的變數名稱相同不會怎麼樣
#     2.一般而言，函數內部對全域變數做修改，此全域變數對於函數外部來說不變
#     3.從函數內部修改全域變數，要先宣告:
#         def function():
#             global a
#             對全域變數a做修改
#         注意:從內部修改全域變數是一件危險的事，不建議這麼做
# 全域變數:函式外部的變數，不管哪裡都有效
#     1.for, while, if, ...內所定義的變數皆為全域
# break:迴圈中遇到break會直接跳出迴圈
# continue:迴圈中遇到continue會直接進入下一次迴圈
#     該次迴圈中continue以下的程式碼均不執行
# 檢驗字串是否為整數:字串名稱.isdigit()
#     如果字串為整數，回傳true；否則回傳false
# file = open("檔案路徑", "模式") 開啟檔案
#     模式有三種 : r(讀取), w(覆寫), a(在原先檔案後新增資料)
# 關於"r"模式:
#     1.file.read() 讀取
#     2.file.readline() 讀取一行(從第一行開始往下讀)
#     3.for line in file:
#          print(line)       這樣就可以一行一行讀出來
#     4.讀取到的會是字串喔
# 關於"w"模式:
#     1.file.write("覆寫內容") 只能是字串!
# 關於"a"模式:
#     1.file.write("欲加入新資料") 只能是字串!
# open("檔案路徑", "模式", encoding="utf-8")這樣就會支援中文
# file.close() 關閉檔案
#     一定要關閉，不然會消耗電腦資源
# with open( , , ) as file: 這樣寫就不用close
# 絕對路徑:從電腦最初始位置寫到檔案名稱 EX:"C:\Users\user\learn\pythonProject\111.txt"
#     注意:\要改成/
# 相對路徑:從目前程式位置延伸 EX:(C:\Users\user\learn\pythonProject)目前程式位置 + \111.txt
# 寫絕對路徑一定可以，寫相對路徑的話111.txt與需要用111.txt的程式需要在同一個資料夾才能用
# "../"可以回到上一個資料夾 EX:"../../111.txt"回到前兩個資料夾的111.txt
# import json 此為json模組
# json是一種檔案格式
# file.write(json.dumps(欲傳送資料, indent = 縮排格數)) 把python原格式轉換成json格式
#     indent可以幫我們自動換行，不需要也可以不用寫
# x = json.loads(file.read()) 把json格式轉換成python原格式
# if x in y: 可以檢驗x是否在y裡，有的話回傳True，否則傳False
# class 類別:可以用來創建自己的資料型態
#     寫法: class 資料型態名稱:
#               pass
# pass:當你的class或是函數內容什麼都沒有時就要加個pass
# object 物件:根據類別class定義出的東西  
#           x = 資料型態名稱() ----->創建資料
#           x.屬性1 = value1
#           x.屬性2 = value2
#               .
#               .
#               .
# 不過以上寫法非常沒效率，用 __init__函數會比較好
# __init__函式:創建資料的時候建會呼叫他
#     寫法: class x:
#               def __init__(self, 屬性1, 屬性2, 屬性3, ...)
#                   self.屬性1 = 屬性1
#                   self.屬性2 = 屬性2
#                   self.屬性3 = 屬性3
#                       .
#                       .
#                       .
#           y = x(屬性1, 屬性2, 屬性3) 創建資料y
# method 方法:在class裡面寫的函式
#     寫法: class x:
#              def method(self, 參數1, ...) 
#                   content
#              y.method(參數1, ...) 使用該method
# 模組引入:
#     1.import f模組 (as f)
#       f.f的函式()       一定要呼叫
#     2.from f模組 import f模組的函式1, 函式2, ...
#       f的函式()         前面不用寫名字
# package 套件:把許多模組裝在同一個資料夾
#     1.資料夾內必須包含__init__.py
#     2.引入套件中模組:
#         (1)import p套件.f模組 (as f)
#            p套件.f模組.f的函式()
#         (2)from 套件 import 模組 (as f)
#            p套件.f模組.f的函式()
#     3.import 套件    會引入__init__
# subpackage 子套件:套件中的套件
#     1.資料夾內必須包含__init__.py
#     2.引入子套件中模組:
#         import p套件.s子套件.f模組 (as f)
#         p套件.子套件.f模組.f的函式()
#     3.import 套件.子套件    會引入__init__
# tuple元組:跟list很像，可以存放多筆資料
#     寫法:(1, 2, 3, ...)
#     與list的差異:
#         1.元組為小括號
#         2.元組一但被創建就無法被修改
# tkinter 為一模組(套件):可以創造GUI程式，也就是圖形介面程式
#     1.寫法:from tkinter import * 
#          window = Tk()        -------------創建一個視窗   
#          對這個視窗的指令要在window = Tk()及window.mainloop()中間
#          window.mainloop()
#     2.window.title("圖形名字") 設定圖形名稱 
#     3.window.geometry("寬x高") 設定圖形寬跟高
#     4.window.maxsize(width="寬度上限", height="高度上限") 設定圖寬高上限
#     5.window.minsize(width="寬度下限", height="高度下限") 設定圖寬高下限
#     6.window.resizable(False, False) 寬高皆無法調整
#     7.x = Label(text="文字", font=("字體", 字大小)) 在視窗上寫字
#       x.pack(side="位置")    字的位置
#       位置可為top, left, right, bottom
#     8.更新設定寫法:
#          (1)x["想更新的設定"] = 更新內容
#          (2)x.config(想更新的設定1 = 更新內容,想更新的設定2 = 更新內容, ...)
#     9.y = Buttom(text="按鈕名稱", font=("", )) 創建按鈕
#       y.pack(side="位置") 按鈕位置
#     10.y = Buttom(text="按鈕名稱", font=("", ), command=指令名稱) 按按鈕就會有功能
#          def 指令名稱
#              指令
#     11.z = Entry(width=寬度, font("", ))  創建對話框
#        z.pack(side="位置")  對話框位置
#     12.def use_spinbox():
#            print(a.get())
#        a = Spinbox(from=n, to=m, width=寬度, command=use_spinbox)   創建範圍n到m的輸入框
#        a.pack()
#     13.def use_scale(value):
#            print(value)
#        b = Scale(from=n, to=m, command=use_scale)   創建範圍n到m拉桿 
#        b.pack()
#     14.def use_checkbuttom():
#            print(check.get())
#        check = IntVar()    有打勾IntVar()回傳1；否則IntVar()回傳0
#        c = Checkbuttom(text="框框名稱", variable=check, font=("", ), command=use_checkbuttom) 創建打勾框框
#        c.pack()
#     15.def use_radiobuttom():
#            print(radio.get())
#        radio = IntVar()
#        d1 = Radiobuttom(text="選擇1", value=1, variable=radio, font=("", ), command=use_checkbuttom) 創建選擇點點1
#        d2 = Radiobuttom(text="選擇2", value=2, variable=radio, font=("", ), command=use_checkbuttom) 創建選擇點點2
#        d1.pack()
#        d2.pack()
# pack()括號內的排版功能
#     1.padx=左右間格數
#     2.pady=上下間格數
#     3.side="位置"
# name.place(x=n,y=m) 把name放在x=n,y=m
# 注意，視窗的原點在左上角，x軸向右為正，y軸向下為正
# 元件的原點也在左上角，要改變的話這樣寫:name.place(anchor="center", x=n, y=m) 元件原點改為中心點
# name.grid(row=n, column=m) 把name放在第n行,第m列
# 利用grid排列要注意，他會把元件黏在一起，元件之間不會有空的row或column
# entry的值如果要轉換成int or float，只能在另一個函數轉，函數外會轉不了
# .get()所取得的值，型態為str