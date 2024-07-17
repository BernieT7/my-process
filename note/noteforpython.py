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
# array跟array運算會一一對應運算喔(ex:[1, 2, 3, 4]*[1, 2, 3, 4] = [1, 4, 9, 16])
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
# inheritance繼承:類別跟類別之間的屬性及方法可以繼承
#    1.例如:class2繼承了class1，class2不用定義就有class1的屬性以及方法
#    2.寫法:class 1:
#               def __init__(self, name, age):
#               def method():
#           class 2(1):
#               pass
#    3.class2可以直接覆寫class1的內容
#    4.若是要在原class1有的屬性下新增屬性:
#           class 2(1):
#               def __init__(self, name, age, score):
#                   1.__init__(self, name, age)
#------------------------也可以這樣寫------------------------
#                   super.__init__()
#                   self.score = score
# 類別與類別之間若是有重疊的屬性及方法就可以使用繼承
# 類別的概念，是可以創建一個自己的類別並自己對自己做改變，如果不是這種情況就要另外在main寫函式    
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
# 字母都是大寫的變數名稱，表示該變數不能更改
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
#     9.y = Button(text="按鈕名稱", font=("", )) 創建按鈕
#       y.pack(side="位置") 按鈕位置
#     10.y = Button(text="按鈕名稱", font=("", ), command=指令名稱) 按按鈕就會有功能
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
#     16.pack()括號內的排版功能
#        1.padx=左右間格數
#        2.pady=上下間格數
#        3.side="位置"
#     17.from tkinter import messagebox
#        (1)messagebox.showinfo(title="標題", message="內容")       創建訊息框
#        (2)messagebox.showerror(title="標題", message="內容")      錯誤訊息框
#        (3)messagebox.showwarning(title="標題", message="內容")    警告訊息框
#        (4)messagebox.askyesno(title="標題", message="內容")       詢問要或不要
#        (5)messagebox.askokcancel(title="標題", message="內容")    詢問確認或取消
#        (6)messagebox.askretrycancel(title="標題", message="內容") 詢問重試或取消
#     18.name.delete(n,m)  可以把輸入框的訊息從第n位到第m-1位刪除
# name.place(x=n,y=m) 把name放在x=n,y=m
# 注意，視窗的原點在左上角，x軸向右為正，y軸向下為正
# 元件的原點也在左上角，要改變的話這樣寫:name.place(anchor="center", x=n, y=m) 元件原點改為中心點
# name.grid(row=n, column=m) 把name放在第n行,第m列
# name.grid(row=n, column=m, columnspan=t) columnspan=n會使元件往右佔t格
# 利用grid排列要注意，他會把元件黏在一起，元件之間不會有空的row或column
# entry的值如果要轉換成int or float，只能在另一個函數轉，函數外會轉不了
# .get()所取得的值，型態為str
# 函式參數預設值:有預設值的函式呼叫函式時可以不用傳入參數
#     寫法:def func(a, b, c=3):         c有預設值
#
#          func(a, b)                呼叫時參數寫a跟b就好
#          func(a, b, c=5)           要改變預設值要寫:c=
# 傳入無限參數的函式:
#     1.寫法:def func(*num):         變數前加上*就可以一次傳入多個參數，並且這些參數會是一組元組的型態
#           
#          func(a, b, c, ...)
#     2.可以與一般變數混著用:def func(a, b, *num):
#
# 傳入無限'指定'參數的函式:
#     1.寫法:def func(**num):        變數前加上**就可以一次傳入多個指定參數，並且這些參數會是字典的型態
# 
#            func(num1=1, num2=2, num3=3, ...)      型態:字典(key=value)
#     2.可以與一般變數混著用:def func(a, b, **num):
# 第三方套件:寫好的套件放到網路上給大家公開使用
# 搜尋第三方套件:
#     1.步驟:google搜尋pypi---->在pypi上搜尋要安裝的第三方套件
#     2.terminal指令: 在terminal輸入
#            (1)pip install 欲安裝套件
#            (2)pip uninstall 欲刪除套件
# tkinter設定元件顏色:bg設定元件背景顏色,fg設定文字顏色
#     1.寫法:x = Label(text="", font=(" ", ), bg="blue", fg="green")
#     2.不一定要寫顏色名字，可以寫顏色編碼(上網找色碼表)
# 第三方套件pillow:可以為視窗加入圖片
#     1.引入:from PIL import ImageTk
#     2.pho = ImageTk.PhotoImage(file="欲上傳圖片")        上傳圖片
#     3.can = Canvas(width=寬, height=高, bg="")           設定畫布
#     4.can.create_image(寬的中心, 高的中心, image=pho)     在畫布上畫出圖片
#     5.can.pack()                                         圖片位置
#     6.在Canvas加入參數highlightthickness 可以把圖片白邊去除
#     7.window.iconphoto(True, 表圖片的變數)  把視窗名稱旁的圖片改掉
# 錯誤處理:
#     1.寫法:try:
#                code 1
#            except:
#                code2        如果code1發生錯誤就執行code2
#     2.except也可以只針對某錯誤類型做處理:
#       寫法:except 錯誤類型
#       補充:印出錯誤訊息:except 錯誤類型 as x:
#                               print(x)
#     3.可以有很多個except
#     4.else: 如果try沒有發生錯誤了就會執行else的程式碼
#     5.finally: 不管try有沒有發生錯誤了都會執行finally的程式碼
# 發起錯誤:raise 錯誤類型("錯誤訊息")
# .get()不能直接用，要先用其他變數接才能用
# 製作動畫遊戲第三方套件pygame:
#     1.寫法:import pygame
#            pygame.init()
#            window = pygame.display.set_mode((寬,高))   創建遊戲介面      -------------創建一個遊戲介面      
#            pygame.display.set_caption("標題")
#            run = True
#            FPS = 60                   一秒更新60次
#            clock = pygame.time.Clock() 創建時鐘
#            while run:
#               clock.tick(FPS)         限制一秒內迴圈最多只會執行幾次
#               #取得輸入
#               for event in pygame.event.get(): 
#                   if event.type == pygame.QUIT:    如果按了視窗右上角的叉叉
#                       run = False
#                   elif event.type == pygame.KEYDOWN:     如果按了鍵盤上的任意按鍵
#                       if event.key == pygame.K_UP:    UP可以改成鍵盤上任意按鍵
#                           y -= 4
#                       elif event.key == pygame.K_DOWN:
#                           y += 4
#---------------------以上寫法只能一次一次按，以下寫法可以按著--------------------------------                       
#                       keys = pygame.key.get_pressed()        如果按鍵被按住會回傳True
#                       if key[pygame.K_UP]:
#                           y -= 4
#                       elif key[pygame.K_DOWN]:
#                           y += 4
#               #遊戲更新
#               x += 0.1
#
#               #畫面顯示
#               window.fill((r, g, b))   介面調色盤(rgb為紅綠藍)
#               pygame.draw.rect(x , (r, g, b), (x, y, h, w))   畫矩形(在哪畫, 顏色, 位置(x, y, 寬, 高))
#                   注意:rect的(x, y)座標為矩形左上角座標 
#               pygame.draw.circle(window, (r, g, b), (x, y), 半徑)   畫圓形(在哪畫, 顏色, 圓心位置, 半徑)
#               pygame.display.update()    顯示    
#            pygame.quit()          關閉遊戲
# font = pygame.font.Font("",n) 引入字體(字體檔案, 大小)
# text = font.render("", True, (rbg)) 訊息內容(內容, 是否要抗鋸齒, 顏色)
#       內容型態必需是str
# window.blit(text,(x, y)) 把訊息畫出來
# img = pygame.image.load("圖片路徑")   引入圖片
# img = pygame.transform.scale(img, (width, height))  把img調整成(width, height)
# window.blit(img, (x, y))  把圖片畫出來
#    注意:後畫的會把先畫的蓋住
# pygame.transform.rotate(img, r)   把圖片旋轉r度
# pygame.transform.flip(img, True, False)   把圖片翻轉(圖片, 水平翻轉, 垂直翻轉)
# pygame.display.set_icon(img)  換視窗左上角的圖片
# pygame的sprite類別可以用來表示遊戲中的所有物件:
# 步驟:(1)先建立一個遊戲物件的class---->
#      (2)讓這個class繼承sprite並且定義img:
#           class Bird(pygame.sprite.Sprite):
#               def __init__(self, x, y, img):
#                   super().__init__()
#                   self.image = img
#                   self.rect = self.image.get_rect()    定位用的，預設在左上角
#                   self.rect.center = ((x, y))          設定物件中心位置
#                             (top,botton,right,left,topleft,topright,bottonleft,bottonright)
#      (3)到main.py創建物件
#      (4)創建sprite群組:group = pygame.sprite.Group()
#      (5)將物件加入群組:group.add(物件名稱)
#      (6)顯示出來:group.draw(window)
# pygame.time.get_ticks()會回傳遊戲開始到現在過了幾毫秒
# 動畫製作的方法直接看bird.py
# self.kill()會把自己刪掉
# pygame.MOUSEBUTTONDOWN 可以偵測有沒有按滑鼠
# event.buttom 按左鍵會回傳1；按右鍵會回傳3 
# pygame.mouse.get_pressed() 可檢驗右滑鼠是否被按住
#    會回傳三個布林值被按回傳True (左鍵, 中鍵, 右鍵)
# elif event.type == pygame.MOUSEMOTION:
#    print(event.pos)                       可以偵測"移動中"滑鼠位置
# pygame.mouse.get_pos()    可以持續偵測滑鼠不論有沒有移動
# 取得物件的x, y座標這樣寫就好self.rect.x or self.rect.y
# pygame.sprite.groupcollide(group1, group2, False, False) 如果group1碰到group2會回傳有值的字典
# ，沒撞到的話就會回傳空字典，後面兩個布林值會判斷要不要被碰到的物件刪掉
# 取得群組中物件資料(型態為列表):group.sprites()
# group.sprites()[i].rect.right 群組中第i個物件座標
# 列表進階用法:
#    1.list[a:b] 取得列表第a到第b-1筆資料
#    2.[:a] 從第0位開始；[a:] 取到最後一位
#    3.str[a:b] 取得字串第a到第b-1筆資料
#    4.[i+n for i in list if 判斷條件] 可以把列表中每一筆符合判斷條件的數據都加n
# 字典進階用法:
#    1.dict.item()回傳字典中所有(key:value) 型態為元組
#    2.用for迴圈可以把key跟value分離:
#        for keys, values in dict.items(): key就會都在keys裡；value都會在values裡
#    3.4.{keys:value + n for keys, values in dict.items() if 判斷條件} 可以把字典中每個符合判斷條件的value都加n, key不變
# pandas數據分析超重要的第三方套件
# data = pandas.read_csv("檔名") 可以讀取CSV檔
# data["column名稱"] 可以讀取此column的所有值
# data["column名稱"].sum() 可以把此column的所有值相加
# data["column名稱"].max() 可以取此column最大值
# data["column名稱"].min() 取最小值
# data["column名稱"].mean() 取平均
# data["column名稱"].map({特定資料: 其覆寫資料, ...}) 可以取得特定資料並將其覆寫
# data[["column1", "column2", ...]] 可以讀取很多column的所有值
# data[a:b] 取得第a行到第b-1行
# data[["column1", "column2", ...]][a:b] 取得多列的第a行到第b-1行
#    data[a:b][["column1", "column2", ...]] 反過來也可以
# column可以轉換成列表或字典: data["column名稱"].to_list()/to_dict()
# row只能轉換成字典data: [a:b].to_dict()
# data[data["column"] ==/</> "想要的資料條件"] 取得某列符合條件的資料
# data[(data["column"] ==/</> "想要的資料條件") & / | (data["column"] ==/</> "想要的資料")] 可以有多個判斷
#    & = and, | = or
# sort_values(by="column") 會把資料由小排到大
# sort_values(by="column", ascending = False) 由大排到小
# data.to_csv("檔名", encoding=utf_8_sig, index=False) 會把資料輸出到檔案
#    index=False會把原本第幾row的數字拿掉
# 直接對data["column名稱"]運算，column內所有值都會進行相同的運算，但不會覆蓋原資料
# data["column名稱"] = data["column名稱"]運算    這樣才會把資料覆蓋
# data["column名稱"].astype(資料型態)    改變整列資料型態
# data["不存在的column"] = 某值    新增新的column
# data.groupby("column1").max()   把column1不同的資料分組並取得各組所有column的最大值
# data.groupby("column1")["column2", "column3", ...] 分組後只取得column2, column3, ...
# data.drop(["column", ...], axis=0or1) 刪除column，axis=1表刪的是列，0是行
# API是別人的電腦寫好的功能包裝起來公開給其他人使用(常常包裝成網址的型式)
# 要使用API必須發送請求，使用第三方套件request
# 請求方法:res = req.get("https:// + base URL + API網址")
# 獲取回應訊息:res.text 型式為字串
# res.json() 會以json格式回傳，比較好用
# pandas的兩個型態:
#    1.2維資料為DataFrame
#    2.1維資料為Series (一行 or 一列)
# pandas.Series([list]) 把list轉換成Series
# pandas.DataFrame(字典)
#    其字典形態要長這樣:{"key1": [], "key2": [], ...}
#    或是:[{key11: value11, key12: value12, key13: value13}
#        ,{key21: value21, key22: value22, key23: value23}
#        ,{key31: value31, key32: value32, key33: value33}
#        , ...]
# 第三方套件schedule可以排程，也就是讓程是在特定時間執行
# schedule.every().second.do(函式) 設定每秒執行一次函式，但還不會執行
# schedule.every(n).seconds.do(函式) 設定每n秒執行一次函式
# schedule.every(n).minites.do(函式) 設定每n分執行一次函式
# schedule.every(n).minites.at(":m").do(函式) 設定每n分m秒執行一次函式
# schedule.every(n).hours.do(函式) 設定每n小時執行一次函式
# schedule.every(n).hours.at("m:s").do(函式) 設定每n小時m分s秒執行一次函式
# schedule.every(n).days.do(函式) 設定每n天執行一次函式
# schedule.every(n).hours.at("m:s:t").do(函式) 設定每n天m小時s分t秒執行一次函式
# schedule.every(n).sunday.at("hh:mm:ss").do(函式) 設定每個禮拜幾的hh小時mm分ss秒執行
# schedule.run_pending()搭配while迴圈 重複執行設定的排程
# 但是while迴圈會執行很多次，但可能真正執行只有一次，為了避免浪費電腦效能，可以這樣:
# import time，在迴圈內利用time模組的time.sleep(n)，這樣成功執行一次後就會休息n秒
# 完整寫法舉例:
#    schedule.every(n).seconds.do(函式, 參數)
#       while True:
#           schedule.run_pending()
#           time.sleep(n)
# 取得目前現在的日期與時間:
#    localtime = time.localtime()
#    result = time.strftime("%Y-%m-%d %I-%M-%S", localtime)
# 如果發送請求的網址需要填寫參數:
#    param = {
#               "Authorization": "CWA-4AACA9C2-1736-4C80-9658-9C64938B1C1A",
#               "locationName": "新竹縣",
#               "elementName": "PoP"
#           }
#    res = req.get("網址", params=param)
# 發送信件可以用
#    import email.message
#    import smtplib
#    
#    my_email = "email_1"
#    password = "密碼" 密碼要去信箱的應用程式密碼取得
# 建立信件:
#    msg = email.message.EmailMessage() 創建信件
#    msg["From"] = my_email 設定信件發送位置
#    msg["To"] = "email_2"
#    msg["Subject"] = "信件主旨"
#    msg.set_content("第一封信件")
# 連線伺服器，從python發送信件:
#    connection = smtplib.SMTP_SSL("伺服器") 連線送件信相的伺服器(上網搜尋yahoo/google信箱伺服器)
#    connection.login(my_email, password) 登入
#    connection.send_message()
#    connection.close()