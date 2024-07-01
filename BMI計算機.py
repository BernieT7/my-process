conti = "Y"

while conti == "Y":
    height = float(input("請輸入您的身高(公分)："))
    weight = float(input("請輸入您的體重："))

    BMI = weight/((height/100)**2)
    BMI = round(BMI, 1)

    if BMI >= 35:
        print(f"您的BMI為：{BMI} (重度肥胖)")
    elif BMI >= 30:
        print(f"您的BMI為：{BMI} (中度肥胖)")
    elif BMI >= 27:
        print(f"您的BMI為：{BMI} (輕度肥胖)")
    elif BMI >= 24:
        print(f"您的BMI為：{BMI} (體種過重)")
    elif BMI >= 18.5:
        print(f"您的BMI為：{BMI} (正常體位)")
    else:
        print(f"您的BMI為：{BMI} (體重過輕)")
    conti = input("請問還要再計算嗎?(請輸入Y or N)").upper()
    
print("謝謝您的使用")