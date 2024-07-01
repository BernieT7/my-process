# 這是一個猜數字的遊戲，範圍是1~100，共五次猜測機會，猜的比答案大或小都會
# 給予提示，如果猜的數字不是整數也會給予提醒
import random
# 與使用者互動
print("歡迎來到猜數字遊戲~")
print("謎底為1~100隨機的一個整數(最多5次猜測機會)")
# 設置隨機答案
ans = random.randint(1, 100)
# 遊戲規則
for i in range(1, 7):
    # 如果猜超過5次就輸了
    if i == 6:
        print("\n你輸了~超過可猜測次數")
        print(f"正確答案為{ans}")
        break
    # 輸入猜測數字
    print(f"第{i}次猜測")
    guess = input("請輸入猜測的數字:")
    # 如果猜的不是整數會被提醒
    if guess.isdigit():
        # 猜太大會被提示小一點
        if int(guess) > ans:
            print("小一點")
        # 猜太小會被提示大一點
        elif int(guess) < ans:
            print("大一點")
        # 猜對了會恭喜你，並不再進入迴圈
        else:
            print("恭喜你猜對了")
            break
    else:
        print("只能輸入整數喔")
        