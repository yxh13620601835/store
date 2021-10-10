'''
    使用while循环实现NxN乘法表的打印。
    authur:yxh
'''
num=int(input("请输入乘法表的层数："))
i=1
while i<=num:
    j = 1
    while j<=i:
        print("%d*%d=%d"%(i,j,i*j),end=" ")
        j += 1
    print()
    i += 1