# 這是一個可以計算BMI、BMR、TDEE的的綜合計算機

# BMI、BMR、TDEE的計算函式
def get_bmi(height, weight):
    BMI = weight / ((height / 100) ** 2)
    BMI = round(BMI, 1)
    return BMI

def get_bmr(sex, height, weight, age):
    if sex == "M":
        BMR = 66 + 13.7*weight + 5*height - 6.8*age
        return BMR
    elif sex == "F":
        BMR = 655 + 9.6*weight + 1.8*height - 4.7*age
        return BMR
    else:
        return "請輸入F or M"

def get_tdee(sex, height, weight, age, times):
    if times == "1":
        TDEE = get_bmr(sex, height, weight, age)*1.2
        return TDEE
    elif times == "2":
        TDEE = get_bmr(sex, height, weight, age) * 1.375
        return TDEE
    elif times == "3":
        TDEE = get_bmr(sex, height, weight, age) * 1.55
        return TDEE
    elif times == "4":
        TDEE = get_bmr(sex, height, weight, age) * 1.725
        return TDEE
    else:
        TDEE = get_bmr(sex, height, weight, age) * 1.9
        return TDEE

# 與使用者互動，了解使用者需要使用何項功能
print("歡迎使用綜合健康計算機~")
print("(1)計算BMI\n(2)計算基礎代謝率BMR\n(3)計算總熱量消耗TDEE")
item = input("請選擇要計算的項目(輸入1 or 2 or3):")

# 計算BMI
if item == "1":
    height = float(input("請輸入您的身高(公分)："))
    weight = float(input("請輸入您的體重："))
    result = get_bmi(height, weight)
    print(result)
# 計算BMR
elif item == "2":
    sex = input("請輸入您的性別(輸入F or M)")
    height = float(input("請輸入您的身高(公分)："))
    weight = float(input("請輸入您的體重："))
    age = int(input("請輸入您的年齡："))
    result = get_bmr(sex, height, weight, age)
    print(result)
# 計算TDEE
else:
    sex = input("請輸入您的性別(輸入F or M):")
    height = float(input("請輸入您的身高(公分)："))
    weight = float(input("請輸入您的體重："))
    age = int(input("請輸入您的年齡："))
    times = input("請問您每周運動頻率為何(輸入1~5)\n(1)久坐、幾乎沒運動\n(2)每周低強度運動1~3天\n(3)每周中強度運動3~5天\n(4)每周高強度運動6~7天\n(5)勞力密集工作或每天高強度工作")
    result = get_tdee(sex, height, weight, age, times)
    print(result)