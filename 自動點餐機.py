# 與使用者互動，開始點餐
print("歡迎使用拉麵點餐機，加好加滿折價20！")
print("(1)鹽味拉麵 $220\n(2)醬油拉麵 $240\n(3)豚骨拉麵 $280")

# 先點拉麵口味
flavor = input("請選擇拉麵口味(輸入1 or 2 or 3)：")

if flavor == "1":
    money = 220
elif flavor == "2":
    money = 240
else:
    money = 280

# 是否加大
size = input("是否加大，豚骨口味+50，其他+30(輸入Y or N):")

if size == "Y":
    if flavor == "1" or flavor == "2":
        money += 30
    else:
        money += 50
else:
    money = money

# 是否加蛋
egg = input("是否加糖心蛋+30(輸入Y or N):")

if egg == "Y":
    money += 30

# 是否加叉燒
meat = input("是否加叉燒+60(輸入Y or N):")

if meat == "Y":
    money += 60

# 判斷是否滿足全加的折價條件
if size == "Y" and egg == "Y" and meat == "Y":
    money -= 20
    print(f"加好加滿折價20，總金額${money}，感謝您的惠顧")
else:
    print(f"總金額${money}，感謝您的惠顧")