from logging import exception
import random
import re
from tkinter import N


global correct
global incorrect
global pull_out_correct
global pull_out_incorrect
global pull_out_random
global now_correct
global now_incorrect
global chosen_card
correct = int(0)
incorrect = int(0)
pull_out_correct = int(0)
pull_out_incorrect = int(0)
pull_out_random = int(0)
all_cards = int(0)
now_correct = int(0)
now_incorrect = int(0)
chosen_card = int(0)


'''0_variable'''


def variable_define_1(
        Variable_index,
        input_string):
    local_Variable = 0
    while True:
        try:
            local_Variable = int(
                input("{0}請輸入{1}:".format(Variable_index, input_string)))
            print(local_Variable)
            break
        except ValueError or TypeError:
            print()
            print("輸入型別錯誤，請輸入大於等於0的「整數」^^")
    while local_Variable < 0:
        print("請輸入大於等於0的「整數」^^")
        local_Variable = input("{0}請輸入{1}:".format(
            Variable_index, input_string))
    return int(local_Variable)


def variable_define_2(
    more_string,
    more_variable,
    less_index,
    less_string,
    less_variable,
):
    while less_variable > more_variable:
        try:
            print(f"請輸入小於{more_string}的「整數」，\n{more_string}目前是{more_variable}")
            less_Variable = input(f"{less_index}請輸入{less_string}:")
            break
        except:
            print(f"請輸入小於{more_string}的「整數」，\n{more_string}目前是{more_variable}")
            less_Variable = input(f"{less_index}請輸入{less_string}:")
    return less_variable


'''function area'''
print("遊戲規則:\
    \n先定義參數(等等會講，下文以「」表示將參數)，\
    \n遊戲開始時，將從「計分卡數」張卡片中抽出「抽出的計分卡數」張卡片、\
    \n從「無計分卡數」張卡片中抽出「抽出的無計分卡數」張卡片、\
    \n從「計分卡片」中與「無計分卡片」中，抽出「抽出隨機卡數」張卡片\
    \n接著，將計分卡片與無計分卡片隨機排列\
    \n再選擇第「選擇第幾張卡片」張卡片\
    \r即可得出是否得分")
print("你需要「分別依序」輸入的參數(「整數」)有:\
    \n1.計分卡數\
    \n2.無計分卡數\
    \n3.抽出的計分卡數\
    \n4.抽出的無計分卡數\
    \n5.抽出隨機卡數\
    \n6.選擇第幾張卡片")
print()
'''game_introduction'''

correct = variable_define_1(
    Variable_index="1.",
    input_string="計分卡數",)

incorrect = variable_define_1(
    Variable_index="2.",
    input_string="無計分卡數",)

all_cards = correct+incorrect
while correct+incorrect == 0:
    print(correct+incorrect)
    print()
    print("總牌數不能為0，請重新輸入")

    correct = variable_define_1(
        Variable_index="1.",
        input_string="計分卡數",)

    incorrect = variable_define_1(
        Variable_index="2.",
        input_string="無計分卡數",)
    print(correct+incorrect)


pull_out_correct = variable_define_1(
    Variable_index="3.",
    input_string="中途抽出的計分卡數")


pull_out_correct = variable_define_2(
    more_string="計分卡數",
    more_variable=correct,
    less_index="3.",
    less_string="中途抽出的計分卡數",
    less_variable=pull_out_correct)


pull_out_incorrect = variable_define_1(
    Variable_index="4.",
    input_string="中途抽出的無計分卡數")

pull_out_incorrect = variable_define_2(
    more_string="無計分卡數",
    more_variable=incorrect,
    less_index="4.",
    less_string="中途抽出的無計分卡數",
    less_variable=pull_out_incorrect)

correct -= pull_out_correct
incorrect -= pull_out_incorrect
all_cards = correct+incorrect

pull_out_random = variable_define_1(
    Variable_index="5.",
    input_string="中途抽出的隨機卡數")

while pull_out_random >= all_cards:
    print("請輸入小於目前總卡數的「整數」，\n目前總卡數目前是%0").format(all_cards)

for i in range(pull_out_random):
    tf = random.randrange(0, 2)
    if correct == 0:
        tf = 1
    if incorrect == 1:
        tf = 0
    if tf == 0:
        correct -= 1
    if tf == 1:
        incorrect -= 1

cards = []
'''
if correct == 0 or incorrect == 0:
    all_cards = correct+incorrect-1
'''
for j in range(all_cards):
    tf = random.randrange(0, 2)
    if now_correct == correct:
        tf = 1
    if now_incorrect == incorrect:
        tf = 0
    if tf == 0:
        cards.insert(j, "T")
        now_correct += 1
    if tf == 1:
        cards.insert(j, "F")
        now_incorrect += 1
print(cards)

chosen_card = variable_define_1(
    Variable_index="6.",
    input_string="選擇第幾張卡片,現在有共有{0}張".format(all_cards))

print(chosen_card)

if cards[chosen_card] == "T":
    print("得分")

if cards[chosen_card] == "F":
    print("哈哈笑死這樣也可以猜錯可以重新投胎洗運氣了")

print(cards[chosen_card])
