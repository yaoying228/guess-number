import random
r = random.randint(10,100)
while True:
    num = input('請輸入數字:')
    num = int(num)
    if num == r:
        print('恭喜你猜對了')
        break
    elif num < r :
        print('你猜的數字比答案小')
    elif num > r:
        print('妳猜的數字比答案大')



