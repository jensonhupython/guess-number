# 2019/6/4
# Practice random
# 產生一個隨機整數 1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "您終於猜對了"
# 猜錯的話 要告訴他 比答案大/小

# Refine version 1
# 每猜一次就告訴 User 目前現在猜第幾次
# Refine version 2
# User 可以決定隨機數字的範圍

import random
start = int(input('請決定隨機範圍數字的起始值:'))
end = int(input('請決定隨機範圍數字的結束值:'))
r = random.randint(start, end)
#print(r)
count = 0
user_guess = 0
while(user_guess != r):
    user_guess = int(input('請猜數字:'))
    count += 1
    if user_guess > r:
        print('Too Big')
    else:
        print('Too Small')
    print('這是你猜的第', count, '次')
print('恭喜答對!', '答案就是:', r)        

