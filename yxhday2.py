'''
猜字游戏
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
任务：猜3次就睡眠 time.sleep(10)
    起始：5000金币，每猜错一次，减去500金币，一直扣完为止。15次没猜中，系统锁定。猜中加3000。
'''
import random
import time
randint = random.randint(1, 30)  # 随机产生的数字
print(randint)
glod = 5000 #起始金币5000
count = 1   #猜数次数
failcount = 0   #猜错次数
while True:
    if glod > 0:
        num=input("请输入一个数字")
        if num.isdigit():
            num=int(num)
            if num == randint:
                print("猜对了，加3000金币")
                glod += 3000
                failcount = 0
            elif num >randint:
                print("猜大了，减500金币")
                glod -= 500
                failcount += 1
            elif num <randint:
                print("猜小了，减500金币")
                glod -= 500
                failcount += 1
        else:
            print("别瞎输入")
    else:
        print("没有金币了，强制退出游戏！")
        break
    if failcount == 15:
        print("猜错15次了，系统已锁定！！")
        while True:
            pass
    if count%3==0:
        time.sleep(10)
        count = 0
    count += 1


