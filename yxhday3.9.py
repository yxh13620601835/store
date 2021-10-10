'''
    编程实现99乘法表的倒叙打印
    author:yxh
'''
j=9
while j>0:
    i = 1
    while j>=i:
        print("%d*%d=%d"%(i,j,i*j),end=" ")
        i += 1
    print()
    j -= 1