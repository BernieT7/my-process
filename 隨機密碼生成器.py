#這是一個可以依照使用者需求生成密碼的程式
import random

# 大小寫字母、數字、符號的列表
letters_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                 "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]

letters_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "+"]

#與使用者互動，了解使用者需要多少大小寫字母、數字以及符號
print("歡迎使用密碼產生器~")
big = int(input("請問需要幾個大寫英文字母?"))
small = int(input("請問需要幾個小寫英文字母?"))
num = int(input("請問需要幾個數字"))
sym = int(input("請問需要幾個符號"))

# 以下隨機照順序選取依照使用者需求的大小寫字母、數字以及符號數量
codes = []

for i in range(0, big):
    codes.append(letters_upper[random.randint(0, 25)])

for i in range(0, small):
    codes.append(letters_lower[random.randint(0, 25)])

for i in range(0, num):
    codes.append(numbers[random.randint(0, 9)])

for i in range(0, sym):
    codes.append(symbols[random.randint(0, 9)])

# 打亂成隨機無序的亂碼
random.shuffle(codes)

ran_code = ""

for code in codes:
    ran_code += code

# result
print(ran_code)