import random

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

rps = [rock, paper, scissor]
con = random.randint(0, 2)

you = input("請輸入字母 s(剪刀)r(石頭)p(布)\n")

if you == "s":
    print(f"你出\n{scissor}\n")
    print("電腦出")
    if con == 0:
        print(str(rps[con]))
        print("你輸了")
    elif con == 1:
        print(str(rps[con]))
        print("你贏了")
    else:
        print(str(rps[con]))
        print("平手")
elif you == "r":
    print(f"你出\n{rock}\n")
    print("電腦出")
    if con == 0:
        print(str(rps[con]))
        print("平手")
    elif con == 1:
        print(str(rps[con]))
        print("你輸了")
    else:
        print(str(rps[con]))
        print("你贏了")
else:
    print(f"你出\n{paper}\n")
    print("電腦出")
    if con == 0:
        print(str(rps[con]))
        print("你贏了")
    elif con == 1:
        print(str(rps[con]))
        print("平手")
    else:
        print(str(rps[con]))
        print("你輸了")