# 這是一個自動單字練習機
import random

# 題庫 
eng_dic = {
    "蘋果": "apple",
    "香蕉": "banana",
    "貓": "cat",
    "狗": "dog",
    "蛋": "egg",
    "食物": "food",
    "遊戲": "game",
    "手": "hand",
    "冰": "ice",
    "果醬": "jam",
    "國王": "king",
    "標籤": "label",
    "郵件": "mail",
    "脖子": "neck",
    "油": "oil",
    "豬": "pig",
    "皇后": "queen"
}

# 使用者自行設定練習次數
practice_time = int(input("請問要練習幾題?"))

# 設定一些初始值
ans = ""
Q_num = 0
correct = 0

# 判斷使用者回答是否正確，便計算答對次數
for i in range(0, practice_time):
    print(f"第{i+1}題:")
    Q_num = random.randint(0, len(list(eng_dic))-1)
    ans = input(f"請問'{list(eng_dic)[Q_num]}'的英文是:")
    if ans == eng_dic[list(eng_dic)[Q_num]]:
        print("恭喜答對\n")
        correct += 1
    else:
        print(f"答錯了~ 答案為{eng_dic[list(eng_dic)[Q_num]]}\n")

#回傳最後作答結果
print(f"總共{practice_time}題 答對了{correct}題")
