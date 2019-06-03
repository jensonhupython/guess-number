# 2019/6/4
# Practice random
# 產生一個隨機整數 1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "您終於猜對了"
# 猜錯的話 要告訴他 比答案大/小

import random

r = random.randint(1,100)
#print(r)

user_guess = 0
while(user_guess != r):
    user_guess = int(input('請猜數字:'))
    if user_guess > r:
        print('Too Big')
    else:
        print('Too Small')

print('恭喜答對!', '答案就是:', r)        

