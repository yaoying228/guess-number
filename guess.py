import random
start =input('請輸入起始範圍值:')
end = input('請輸入結束範圍值:')
start = int(start)
end = int(end)

r = random.randint(start, end)

count = 0
while True:
    count = count + 1       # count += 1 這是寫法
    num = input('請輸入數字:')
    num = int(num)
    if num == r:
        print('恭喜你猜對了')
        print('這是你猜的', count , '次')
        break
    elif num < r :
        print('你猜的數字比答案小')
    elif num > r:
        print('妳猜的數字比答案大')
    print('這是你猜的', count , '次')




