'''
    用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
    author:yxh
'''

sum=0
for i in range(1,21):
    ride = 1
    for j in range(1,i+1):
        ride *= j #求i的阶乘
    sum += ride
print("1! +2!+3!+…..+20!=%d"%sum)